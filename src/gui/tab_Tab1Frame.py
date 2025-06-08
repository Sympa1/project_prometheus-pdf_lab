import customtkinter as ctk

class Tab1Frame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.checkbox_1 = ctk.CTkCheckBox(self, text="Checkbox 1")
        self.checkbox_1.pack(anchor="w", padx=10, pady=(10, 0))
        self.checkbox_2 = ctk.CTkCheckBox(self, text="Checkbox 2")
        self.checkbox_2.pack(anchor="w", padx=10, pady=(10, 0))