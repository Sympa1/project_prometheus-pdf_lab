import customtkinter as ctk

class TabSplitten(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        ctk.CTkLabel(self, text="Inhalt Tab Splitten").pack(padx=10, pady=10)