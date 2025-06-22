import customtkinter as ctk
from tkinter import filedialog
import os
from classes.cl_PdfUtility import PdfUtility
from .cl_Messagebox import Messagebox
from classes.cl_Utils import Utils

# TODO: Implementiere die Logik zum Mergen von PDFs im Backend.
#  Aktuell ist es nur eine Simulation, die eine Messagebox anzeigt.
# TODO: Eine Wrapper Methode für das Mergen von PDFs könnte hier sinnvoll sein, da der Button nacheinander mehrere
#  Aufgaben ausführen soll.
#  Den Speicherort der gemergen PDF-Datei abfragen, die Dateien zusammenführen, die Datei speichern und dann eine
#  Messagebox anzeigen.

class TabMergen(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.file_list = []

        # Hole die Fensterbreite und -höhe aus der Config (über das Hauptfenster)
        window_width = getattr(master.master, "window_width", 800)  # Fallback auf 800
        window_height = getattr(master.master, "window_height", 600)  # Fallback auf 600

        # Button zum Hinzufügen von PDF-Dateien
        self.add_button = ctk.CTkButton(self, text="PDF hinzufügen", command=self.add_file)
        self.add_button.pack(anchor="w", padx=10, pady=(10, 0))

        # Textbox zur Anzeige der hinzugefügten PDF-Dateipfade
        # die Größe orientiert sich an der Fenstergröße
        textbox_width = max(window_width - 60, 300)
        textbox_height = max(int(window_height / 2), 100)
        self.listbox = ctk.CTkTextbox(self, height=textbox_height, width=textbox_width)
        self.listbox.pack(anchor="w", padx=10, pady=(10, 0), fill="x") # fill=x sorgt für ein responsive anmutendes Verhalten
        self.listbox.configure(state="disabled")

        # Button zum Starten des mergen's der PDFs
        self.merge_button = ctk.CTkButton(self, text="PDFs zusammenführen", command=self.merge_pdfs)
        self.merge_button.pack(anchor="e", padx=10, pady=(15, 10))

    def add_file(self):
        # Standardverzeichnis: Dokumente-Ordner des Users (deutsch/englisch)
        documents_dir = os.path.expanduser("~/Dokumente")
        if not os.path.exists(documents_dir):
            documents_dir = os.path.expanduser("~/Documents")  # Fallback für englische Systeme

        # Öffne Dateidialog zur Auswahl von PDF-Dateien
        filenames = filedialog.askopenfilenames(
            title="PDF auswählen",
            filetypes=[("PDF-Dateien", "*.pdf")],
            initialdir=documents_dir
        )
        # Füge neue Dateien zur Liste hinzu (keine Duplikate)
        for file in filenames:
            if file not in self.file_list:
                self.file_list.append(file)
        self.update_listbox()

    def update_listbox(self):
        # Aktualisiere die Textbox mit allen aktuell ausgewählten PDF-Dateipfaden
        self.listbox.configure(state="normal")
        self.listbox.delete("1.0", "end")
        for file in self.file_list:
            self.listbox.insert("end", file + "\n")
        self.listbox.configure(state="disabled")

    def mergee_pdfs(self):
        # Öffne Filedialog für den Zielspeicherort des zusammengeführten PDFs
        documents_dir = os.path.expanduser("~/Dokumente")
        if not os.path.exists(documents_dir):
            documents_dir = os.path.expanduser("~/Documents")
        save_path = filedialog.asksaveasfilename(
            title="Ziel-PDF speichern",
            defaultextension=".pdf",
            filetypes=[("PDF-Dateien", "*.pdf")],
            initialdir=documents_dir
        )

        # TODO: Macht ein if else hier Sinn? Wenn der Nutzer keinen Speicherort auswählt, wird
        #  die Funktion abgebrochen und es wird keine Messagebox angezeigt.
        #if save_path:
            # Hier würdest du das eigentliche Mergen der PDFs implementieren
    def merge_pdfs(self):
        # prüfen ob die Liste leer(null) ist
        if not self.file_list:
            Messagebox("PDF zusammenführen", "Keine PDF-Dateien zum Zusammenführen ausgewählt.").messagebox_warning()
            return

        # Öffne Filedialog für den Zielspeicherort des zusammengeführten PDFs
        documents_dir = os.path.expanduser("~/Dokumente")
        if not os.path.exists(documents_dir):
            documents_dir = os.path.expanduser("~/Documents")
        save_path = filedialog.asksaveasfilename(
            title="Ziel-PDF speichern",
            defaultextension=".pdf",
            filetypes=[("PDF-Dateien", "*.pdf")],
            initialdir=documents_dir
        )

        # prüfen ob der string nicht leer (null) ist
        if save_path:
            try:
                # merge der PDFs
                PdfUtility.merge_pdf(self.file_list, save_path)

                # Rückmeldung an den User, dass die PDFs germeged wurden
                Messagebox("PDF zusammenführen", f"PDFs wurden erfolgreich zusammengeführt und gespeichert"
                                                 f"unter:\n{save_path}").messagebox_info()
            except Exception as e:
                # Fehlermeldung falls beim Mergen etwas schiefgeht
                Messagebox("Fehler", f"Fehler beim Zusammenführen der PDFs:\n{str(e)}").messagebox_error()
                Utils.write_to_log(f"Fehler beim Zusammenführen der PDFs:\n{str(e)}")
        # Wenn save_path leer ist (Dialog abgebrochen), passiert nichts 