import customtkinter as ctk
from tkinter import filedialog
import os
from classes.cl_PdfUtility import PdfUtility
from .cl_Messagebox import Messagebox
from classes.cl_Utils import Utils

# TODO: Ich brauche einen "reset" der PDF Liste nach einem splitten per Button
# TODO: Eine Progressbar für den Splittenprozess
# TODO: Code optimieren

class TabSplitten(ctk.CTkFrame):
    """
    Tab-Klasse für das Splitten von PDF-Dateien.
    Erbt von ctk.CTkFrame und stellt die GUI-Komponenten für die PDF-Split-Funktionalität bereit.
    """

    def __init__(self, master):
        """
        Initialisiert den TabSplitten Frame mit allen GUI-Elementen.

        Args:
            master: Das übergeordnete Widget.
        """
        super().__init__(master)
        self.input_pdf = None  # Pfad zur ausgewählten PDF-Datei
        self.output_part1 = None  # Pfad für den ersten Teil der gesplitteten PDF
        self.output_part2 = None  # Pfad für den zweiten Teil der gesplitteten PDF
        self.pdf_utility = PdfUtility()  # Utility-Objekt für PDF-Operationen

        # Fensterdimensionen aus der Konfiguration laden
        window_width = getattr(master.master, "window_width", 800)  # Fallback auf 800
        window_height = getattr(master.master, "window_height", 600)  # Fallback auf 600

        # === GUI-ELEMENTE ERSTELLEN ===

        # Button zum Auswählen der zu splittenden PDF-Datei
        self.select_file_button = ctk.CTkButton(self, text="PDF zum Splitten auswählen", command=self.select_input_pdf)
        self.select_file_button.pack(anchor="w", padx=10, pady=(10, 0))

        # Label zur Anzeige der ausgewählten PDF-Datei
        self.file_label = ctk.CTkLabel(self, text="Keine Datei ausgewählt")
        self.file_label.pack(anchor="w", padx=10, pady=(5, 0))

        # Label für Seitenzahl-Info
        self.page_info_label = ctk.CTkLabel(self, text="")
        self.page_info_label.pack(anchor="w", padx=10, pady=(5, 0))

        # Frame für die Spinbox (Seitenzahl zum Splitten)
        self.spinbox_frame = ctk.CTkFrame(self)
        self.spinbox_frame.pack(anchor="w", padx=10, pady=(10, 0))

        # Label für Spinbox
        self.spinbox_label = ctk.CTkLabel(self.spinbox_frame, text="Splitten nach Seite:")
        self.spinbox_label.pack(side="left", padx=(10, 5), pady=10)

        # Custom Spinbox mit - Button, Entry und + Button
        self.minus_button = ctk.CTkButton(self.spinbox_frame, text="-", width=30, command=self.decrease_value)
        self.minus_button.pack(side="left", padx=2, pady=10)

        self.page_entry = ctk.CTkEntry(self.spinbox_frame, width=60, justify="center")
        self.page_entry.pack(side="left", padx=2, pady=10)
        self.page_entry.insert(0, "1")
        self.page_entry.bind("<KeyRelease>", self.validate_page_number)

        self.plus_button = ctk.CTkButton(self.spinbox_frame, text="+", width=30, command=self.increase_value)
        self.plus_button.pack(side="left", padx=2, pady=10)

        # Frame für Output-Pfade
        self.output_frame = ctk.CTkFrame(self)
        self.output_frame.pack(anchor="w", padx=10, pady=(10, 0), fill="x")

        # Output Teil 1
        self.output1_label = ctk.CTkLabel(self.output_frame, text="Output Teil 1: Standardpfad wird verwendet")
        self.output1_label.pack(anchor="w", padx=10, pady=(10, 5))

        self.select_output1_button = ctk.CTkButton(self.output_frame, text="Pfad für Teil 1 ändern", command=self.select_output1_pdf)
        self.select_output1_button.pack(anchor="w", padx=10, pady=(0, 5))

        # Output Teil 2
        self.output2_label = ctk.CTkLabel(self.output_frame, text="Output Teil 2: Standardpfad wird verwendet")
        self.output2_label.pack(anchor="w", padx=10, pady=(5, 5))

        self.select_output2_button = ctk.CTkButton(self.output_frame, text="Pfad für Teil 2 ändern", command=self.select_output2_pdf)
        self.select_output2_button.pack(anchor="w", padx=10, pady=(0, 10))

        # Button zum Starten des Splittens
        self.split_button = ctk.CTkButton(self, text="PDF splitten", command=self.split_pdf)
        self.split_button.pack(anchor="e", padx=10, pady=(15, 10))

        # Initial Button deaktivieren (wird erst bei Dateiauswahl aktiviert)
        self.split_button.configure(state="disabled")

    def select_input_pdf(self):
        """
        Öffnet einen Dateidialog zur Auswahl einer PDF-Datei, die gesplittet werden soll.
        Zeigt Dateiname und Seitenzahl an und setzt Standard-Ausgabepfade.
        """
        documents_dir = os.path.expanduser("~/Dokumente")
        if not os.path.exists(documents_dir):
            documents_dir = os.path.expanduser("~/Documents")  # Fallback für englische Systeme

        filename = filedialog.askopenfilename(
            title="PDF zum Splitten auswählen",
            filetypes=[("PDF-Dateien", "*.pdf")],
            initialdir=documents_dir
        )

        if filename:
            self.input_pdf = filename
            self.file_label.configure(text=f"Ausgewählt: {os.path.basename(filename)}")

            try:
                # Seitenzahl ermitteln und anzeigen
                page_count = self.pdf_utility.get_page_count(filename)
                self.page_info_label.configure(text=f"Gesamt: {page_count} Seiten")

                # Standard-Ausgabepfade setzen
                input_dir = os.path.dirname(filename)
                base_name = os.path.splitext(os.path.basename(filename))[0]
                self.output_part1 = os.path.join(input_dir, f"{base_name}_part1.pdf")
                self.output_part2 = os.path.join(input_dir, f"{base_name}_part2.pdf")
                self.output1_label.configure(text=f"Output Teil 1: {base_name}_part1.pdf")
                self.output2_label.configure(text=f"Output Teil 2: {base_name}_part2.pdf")

                # Split-Button aktivieren
                self.split_button.configure(state="normal")

            except Exception as e:
                Messagebox("Fehler", f"Fehler beim Lesen der PDF: {str(e)}").messagebox_error()
                Utils.write_to_log(f"Fehler beim Lesen der PDF: {str(e)}")
                self.reset_ui()
        else:
            self.reset_ui()

    def select_output1_pdf(self):
        """
        Öffnet einen Dialog zur Auswahl des Speicherorts für den ersten Teil der gesplitteten PDF.
        Aktualisiert das zugehörige Label.
        """
        if not self.input_pdf:
            return

        initial_dir = os.path.dirname(self.input_pdf)
        filename = filedialog.asksaveasfilename(
            title="Speicherort für Teil 1",
            filetypes=[("PDF-Dateien", "*.pdf")],
            initialdir=initial_dir,
            defaultextension=".pdf"
        )

        if filename:
            self.output_part1 = filename
            self.output1_label.configure(text=f"Output Teil 1: {os.path.basename(filename)}")

    def select_output2_pdf(self):
        """
        Öffnet einen Dialog zur Auswahl des Speicherorts für den zweiten Teil der gesplitteten PDF.
        Aktualisiert das zugehörige Label.
        """
        if not self.input_pdf:
            return

        initial_dir = os.path.dirname(self.input_pdf)
        filename = filedialog.asksaveasfilename(
            title="Speicherort für Teil 2",
            filetypes=[("PDF-Dateien", "*.pdf")],
            initialdir=initial_dir,
            defaultextension=".pdf"
        )

        if filename:
            self.output_part2 = filename
            self.output2_label.configure(text=f"Output Teil 2: {os.path.basename(filename)}")

    def increase_value(self):
        """
        Erhöht den Wert im Seitenzahl-Eingabefeld um 1, solange das Maximum nicht überschritten wird.
        """
        try:
            current_value = int(self.page_entry.get())
            if self.input_pdf:
                max_pages = self.pdf_utility.get_page_count(self.input_pdf) - 1
                if current_value < max_pages:
                    self.page_entry.delete(0, "end")
                    self.page_entry.insert(0, str(current_value + 1))
        except ValueError:
            self.page_entry.delete(0, "end")
            self.page_entry.insert(0, "1")

    def decrease_value(self):
        """
        Verringert den Wert im Seitenzahl-Eingabefeld um 1, mindestens jedoch auf 1.
        """
        try:
            current_value = int(self.page_entry.get())
            if current_value > 1:
                self.page_entry.delete(0, "end")
                self.page_entry.insert(0, str(current_value - 1))
        except ValueError:
            self.page_entry.delete(0, "end")
            self.page_entry.insert(0, "1")

    def validate_page_number(self, event=None):
        """
        Validiert die Eingabe im Seitenzahl-Eingabefeld.
        Stellt sicher, dass nur gültige Zahlen eingegeben werden und der Wert im erlaubten Bereich liegt.
        """
        try:
            value = self.page_entry.get()
            if value:
                page_num = int(value)
                if self.input_pdf:
                    max_pages = self.pdf_utility.get_page_count(self.input_pdf) - 1
                    if page_num < 1:
                        self.page_entry.delete(0, "end")
                        self.page_entry.insert(0, "1")
                    elif page_num > max_pages:
                        self.page_entry.delete(0, "end")
                        self.page_entry.insert(0, str(max_pages))
        except ValueError:
            # Nur Zahlen erlauben
            valid_chars = ''.join(c for c in self.page_entry.get() if c.isdigit())
            if valid_chars:
                self.page_entry.delete(0, "end")
                self.page_entry.insert(0, valid_chars)
            else:
                self.page_entry.delete(0, "end")
                self.page_entry.insert(0, "1")

    def split_pdf(self):
        """
        Führt das Splitten der ausgewählten PDF-Datei durch.
        Validiert die Eingaben, führt den Split-Prozess durch und zeigt entsprechende Rückmeldungen an.
        """
        if not self.input_pdf:
            Messagebox("PDF splitten", "Keine PDF-Datei zum Splitten ausgewählt.").messagebox_warning()
            return

        if not self.output_part1 or not self.output_part2:
            Messagebox("Fehler", "Bitte wählen Sie Ausgabepfade für beide Teile aus.").messagebox_error()
            return

        try:
            split_at = int(self.page_entry.get())

            # Überprüfen, ob die Output-Verzeichnisse existieren
            os.makedirs(os.path.dirname(self.output_part1), exist_ok=True)
            os.makedirs(os.path.dirname(self.output_part2), exist_ok=True)

            # PDF splitten
            PdfUtility.split_pdf(self.input_pdf, self.output_part1, self.output_part2, split_at)

            # Erfolgsmeldung an den Benutzer
            Messagebox("PDF splitten", f"PDF wurde erfolgreich gesplittet und gespeichert unter:\n"
                                       f"Teil 1: {self.output_part1}\n"
                                       f"Teil 2: {self.output_part2}").messagebox_info()

        except Exception as e:
            # Fehlermeldung bei Problemen während des Split-Prozesses
            Messagebox("Fehler", f"Fehler beim Splitten der PDF:\n{str(e)}").messagebox_error()
            Utils.write_to_log(f"Fehler beim Splitten der PDF:\n{str(e)}")

    def reset_ui(self):
        """
        Setzt die UI auf den Ausgangszustand zurück.
        """
        self.input_pdf = None
        self.output_part1 = None
        self.output_part2 = None
        self.file_label.configure(text="Keine Datei ausgewählt")
        self.page_info_label.configure(text="")
        self.output1_label.configure(text="Output Teil 1: Standardpfad wird verwendet")
        self.output2_label.configure(text="Output Teil 2: Standardpfad wird verwendet")
        self.page_entry.delete(0, "end")
        self.page_entry.insert(0, "1")
        self.split_button.configure(state="disabled")