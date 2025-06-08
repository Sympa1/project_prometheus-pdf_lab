import customtkinter as ctk
from .tab_Tab1Frame import Tab1Frame
from .tab_Tab2Frame import Tab2Frame
from .tab_Tab3Frame import Tab3Frame

class MyTabView(ctk.CTkTabview):
    def __init__(self, master):
        super().__init__(master)
        self.add("Tab 1")
        self.add("Tab 2")
        self.add("Tab 3")

        # Tab-Inhalte als Frames einfügen
        Tab1Frame(self.tab("Tab 1")).pack(fill="both", expand=True)
        Tab2Frame(self.tab("Tab 2")).pack(fill="both", expand=True)
        Tab3Frame(self.tab("Tab 3")).pack(fill="both", expand=True)