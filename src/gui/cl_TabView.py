import customtkinter as ctk
from .cl_TabMergen import TabMergen
from .cl_TabSplitten import TabSplitten
from .cl_TabVerschluesseln import TabVerschluesseln

class TabView(ctk.CTkTabview):
    """TabView ist ein Tab-Container, der verschiedene PDF-bezogene Funktionen wie Mergen, Splitten und Verschlüsseln bereitstellt.
    """
    
    def __init__(self, master):
        super().__init__(master)
        # Erstelle drei Tabs für die verschiedenen PDF-Funktionen
        self.add("PDF's mergen")
        self.add("PDF's splitten")
        self.add("PDF's verschlüsseln")

        # Füge die jeweiligen Frames als Inhalt in die Tabs ein.
        # Durch fill="both" und expand=True wachsen die Frames mit dem Tab und Fenster mit (responsives Verhalten).
        TabMergen(self.tab("PDF's mergen")).pack(fill="both", expand=True)
        TabSplitten(self.tab("PDF's splitten")).pack(fill="both", expand=True)
        TabVerschluesseln(self.tab("PDF's verschlüsseln")).pack(fill="both", expand=True)