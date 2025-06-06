import customtkinter as ctk

from .cl_MyCheckboxFrame import MyCheckboxFrame
from .cl_Theme import Theme
from classes import Utils
from .cl_Messagebox import Messagebox

class Gui(ctk.CTk):  
    def __init__(self):
        super().__init__()

        self.title("PyPDFCrafter")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.config = Utils()

        # Fenstergröße aus Config laden
        self.window_width = self.config.get_config("window_width")
        self.window_height = self.config.get_config("window_height")
        self.geometry(f"{self.window_width}x{self.window_height}")

        # Theme - default Darkemode
        self.theme_status = f"{self.config.get_config("theme")}"
        ctk.set_appearance_mode(self.theme_status)

        # Checkboxframe
        self.checkbox_frame = MyCheckboxFrame(self)
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")

        # Dark / Lightmode Button Frame
        self.theme_frame = Theme(self, self.config)
        self.theme_frame.grid(row=0, column=1, padx=0, pady=(0, 5), sticky="ne")

        self.button = ctk.CTkButton(self, text="Beenden", hover=True, width=20, command=self.on_close)
        self.button.grid(row=3, column=1, padx=10, pady=10)

        # Nach dem Aufbau prüfen ob config neu erstellt wurde
        self.after(100, self.check_config_created)

        # Event-Handler für das Schließen des Fensters setzen
        # Speichert die aktuelle Fenstergröße in der Config beim Beenden
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def check_config_created(self):
        if getattr(self.config, "config_created", False):
            Messagebox("Info", "Die Konfigurationsdatei 'config.json' wurde nicht gefunden. Standardwerte wurden gesetzt.").messagebox_info()

    def on_close(self):
        """Wird beim Schließen des Fensters aufgerufen. Speichert die aktuelle Fenstergröße."""
        width = self.winfo_width()
        height = self.winfo_height()
        self.config.set_config("window_width", width)
        self.config.set_config("window_height", height)
        self.destroy()