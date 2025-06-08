import customtkinter as ctk

class Tab3Frame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        ctk.CTkLabel(self, text="Inhalt Tab 3").pack(padx=10, pady=10)