import customtkinter as ctk
from tkinter import filedialog
import os
from .cl_Messagebox import Messagebox

class TabVerEntschluesseln(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.selected_file = None

        # Button zum Auswählen einer PDF-Datei
        self.select_button = ctk.CTkButton(self, text="PDF auswählen", command=self.select_pdf, width=180)
        self.select_button.pack(padx=20, pady=(20, 5), anchor="w")

        # Label zur Anzeige des aktuell gewählten Dateipfads
        self.file_label = ctk.CTkLabel(self, text="Keine Datei ausgewählt", anchor="w")
        self.file_label.pack(padx=20, pady=(0, 15), anchor="w")

        # Eingabefeld für das Passwort (standardmäßig als Sternchen angezeigt)
        self.password_entry = ctk.CTkEntry(self, placeholder_text="Passwort", show="*")
        self.password_entry.pack(padx=20, pady=(0, 5), anchor="w")

        # Checkbox zum Anzeigen/Verbergen des Passworts
        self.show_pw_var = ctk.BooleanVar()
        self.show_pw_checkbox = ctk.CTkCheckBox(self, text="Passwort anzeigen", variable=self.show_pw_var, command=self.toggle_password)
        self.show_pw_checkbox.pack(padx=20, pady=(0, 20), anchor="w")

        # Button zum Verschlüsseln der PDF
        self.encrypt_button = ctk.CTkButton(self, text="PDF verschlüsseln", command=self.encrypt_pdf, width=180)
        self.encrypt_button.pack(padx=20, pady=(0, 10), anchor="w")

        # Button zum Entschlüsseln der PDF
        self.decrypt_button = ctk.CTkButton(self, text="PDF entschlüsseln", command=self.decrypt_pdf, width=180)
        self.decrypt_button.pack(padx=20, pady=(0, 20), anchor="w")

    def select_pdf(self):
        # Öffnet einen Dateidialog zur Auswahl einer PDF-Datei
        documents_dir = os.path.expanduser("~/Dokumente")
        if not os.path.exists(documents_dir):
            documents_dir = os.path.expanduser("~/Documents")
        filename = filedialog.askopenfilename(
            title="PDF auswählen",
            filetypes=[("PDF-Dateien", "*.pdf")],
            initialdir=documents_dir
        )
        # Zeigt den gewählten Dateipfad im Label an
        if filename:
            self.selected_file = filename
            self.file_label.configure(text=filename)
        else:
            self.selected_file = None
            self.file_label.configure(text="Keine Datei ausgewählt")

    def toggle_password(self):
        # Zeigt oder verbirgt das Passwort im Eingabefeld je nach Checkbox-Status
        if self.show_pw_var.get():
            self.password_entry.configure(show="")
        else:
            self.password_entry.configure(show="*")

    def encrypt_pdf(self):
        # Prüft, ob eine Datei und ein Passwort gewählt wurden, und öffnet einen Speichern-Dialog
        if not self.selected_file:
            Messagebox("Fehler", "Bitte zuerst eine PDF-Datei auswählen!").messagebox_warning()
            return
        password = self.password_entry.get()
        if not password:
            Messagebox("Fehler", "Bitte ein Passwort eingeben!").messagebox_warning()
            return
        documents_dir = os.path.expanduser("~/Dokumente")
        if not os.path.exists(documents_dir):
            documents_dir = os.path.expanduser("~/Documents")
        save_path = filedialog.asksaveasfilename(
            title="Verschlüsselte PDF speichern",
            defaultextension=".pdf",
            filetypes=[("PDF-Dateien", "*.pdf")],
            initialdir=documents_dir
        )
        # Zeigt eine Info-Messagebox nach dem (simulierten) Verschlüsseln
        if save_path:
            # Hier würdest du das Verschlüsseln implementieren
            Messagebox("PDF verschlüsseln", f"PDF würde verschlüsselt gespeichert unter:\n{save_path}").messagebox_info()

    def decrypt_pdf(self):
        # Prüft, ob eine Datei und ein Passwort gewählt wurden, und öffnet einen Speichern-Dialog
        if not self.selected_file:
            Messagebox("Fehler", "Bitte zuerst eine PDF-Datei auswählen!").messagebox_warning()
            return
        password = self.password_entry.get()
        if not password:
            Messagebox("Fehler", "Bitte ein Passwort eingeben!").messagebox_warning()
            return
        documents_dir = os.path.expanduser("~/Dokumente")
        if not os.path.exists(documents_dir):
            documents_dir = os.path.expanduser("~/Documents")
        save_path = filedialog.asksaveasfilename(
            title="Entschlüsselte PDF speichern",
            defaultextension=".pdf",
            filetypes=[("PDF-Dateien", "*.pdf")],
            initialdir=documents_dir
        )
        # Zeigt eine Info-Messagebox nach dem (simulierten) Entschlüsseln
        if save_path:
            # Hier würdest du das Entschlüsseln implementieren
            Messagebox("PDF entschlüsseln", f"PDF würde entschlüsselt gespeichert unter:\n{save_path}").messagebox_info()