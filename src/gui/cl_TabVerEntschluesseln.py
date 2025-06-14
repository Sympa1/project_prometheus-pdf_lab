import customtkinter as ctk

class TabVerEntschluesseln(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        ctk.CTkLabel(self, text="Inhalt Tab Ver-/Entschlüsseln").pack(padx=10, pady=10)