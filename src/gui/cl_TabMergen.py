import customtkinter as ctk
from tkinter import filedialog
import os
from .cl_Messagebox import Messagebox

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
        # Die Größe orientiert sich an der Fenstergröße
        textbox_width = max(window_width - 60, 300)
        textbox_height = max(int(window_height / 2), 100)
        self.listbox = ctk.CTkTextbox(self, height=textbox_height, width=textbox_width)
        self.listbox.pack(anchor="w", padx=10, pady=(10, 0), fill="x") # fill=x sorgt für ein responsive anmutendes Verhalten
        self.listbox.configure(state="disabled")

        # Button zum Starten des Mergings der PDFs
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

    def merge_pdfs(self):
        # Öffne Filedialog für den Zielspeicherort der zusammengeführten PDF
        documents_dir = os.path.expanduser("~/Dokumente")
        if not os.path.exists(documents_dir):
            documents_dir = os.path.expanduser("~/Documents")
        save_path = filedialog.asksaveasfilename(
            title="Ziel-PDF speichern",
            defaultextension=".pdf",
            filetypes=[("PDF-Dateien", "*.pdf")],
            initialdir=documents_dir
        )
        if save_path:
            # Hier würdest du das eigentliche Mergen der PDFs implementieren
            # Rückmeldung an den Nutzer per Messagebox
            Messagebox("PDF zusammenführen", f"PDFs würden gemerged und gespeichert unter:\n{save_path}").messagebox_info()