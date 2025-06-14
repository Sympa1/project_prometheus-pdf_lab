import customtkinter as ctk
from .cl_TabMergen import TabMergen
from .cl_TabSplitten import TabSplitten
from .cl_TabVerEntschluesseln import TabVerEntschluesseln

class TabView(ctk.CTkTabview):
    def __init__(self, master):
        super().__init__(master)
        self.add("PDF's mergen")
        self.add("PDF's splitten")
        self.add("PDF's ver/entschlüsseln")

        # Tab-Inhalte als Frames einfügen
        TabMergen(self.tab("PDF's mergen")).pack(fill="both", expand=True)
        TabSplitten(self.tab("PDF's splitten")).pack(fill="both", expand=True)
        TabVerEntschluesseln(self.tab("PDF's ver/entschlüsseln")).pack(fill="both", expand=True)