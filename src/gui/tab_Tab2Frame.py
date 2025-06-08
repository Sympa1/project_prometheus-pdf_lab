import customtkinter as ctk

class Tab2Frame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        ctk.CTkLabel(self, text="Inhalt Tab 2").pack(padx=10, pady=10)