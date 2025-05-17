import customtkinter as ctk

from .cl_MyCheckboxFrame import MyCheckboxFrame
from .cl_DarkLightmode import DarkLightmode

class Gui(ctk.CTk):  
    def __init__(self):
        super().__init__()

        self.title("PyPDFCrafter")
        self.geometry("400x180")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Standard Darkmode
        self.dl_status = "dark"
        ctk.set_appearance_mode(self.dl_status)

        # Checkboxframe
        self.checkbox_frame = MyCheckboxFrame(self)
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")

        # Dark / Lightmode Button Frame
        self.dl_frame = DarkLightmode(self)
        self.dl_frame.grid(row=0, column=1, padx=10, pady=(0, 0), sticky="ne")

        self.button = ctk.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    def button_callback(self):
        print("button pressed")