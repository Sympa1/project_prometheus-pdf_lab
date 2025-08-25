import customtkinter as ctk
import os
import sys
from PIL import Image
from classes import Utils


def resource_path(relative_path: str) -> str:
    """
    Liefert den absoluten Pfad zu einer Resource.
    Funktioniert sowohl beim normalen Start (VSCode/PyCharm)
    als auch bei PyInstaller (--onefile).
    """
    if hasattr(sys, "_MEIPASS"):  # PyInstaller Temp-Ordner
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


class Theme(ctk.CTkFrame):
    """Theme ist ein Frame, der es ermöglicht, zwischen Dark und Light Mode zu wechseln.
    """
    def __init__(self, master, config):
        super().__init__(master)
        self.config = config

        # Hintergrund wie Hauptfenster
        self.configure(fg_color=master.cget("fg_color"))

        try:
            sun_path = resource_path("data/img/sunny-outline.png")
            moon_path = resource_path("data/img/moon-outline.png")

            self.sun_image = ctk.CTkImage(Image.open(sun_path), size=(32, 32))
            self.moon_image = ctk.CTkImage(Image.open(moon_path), size=(32, 32))
        except Exception as e:
            Utils.write_to_log(f"Bilder nicht gefunden! {e}")
            self.sun_image = None
            self.moon_image = None

        # Innerer Frame ohne Dehnung
        self.inner_frame = ctk.CTkFrame(self, fg_color="transparent", width=80, height=40)
        self.inner_frame.pack(padx=0, pady=0, anchor="w")
        self.inner_frame.pack_propagate(False)

        # Switch
        self.switch = ctk.CTkSwitch(self.inner_frame, text="", hover=True, command=self.toggle_mode)
        self.switch.place(x=0, y=4)

        # Theme Bild
        self.image_label = ctk.CTkLabel(self.inner_frame, text="")
        self.image_label.place(x=45, y=0)

        # Status aus Config lesen
        theme_from_config = self.config.get_config("theme")
        if theme_from_config == "dark":
            self.switch.select()  # Switch AN
            if self.moon_image:
                self.image_label.configure(image=self.moon_image)
            ctk.set_appearance_mode("dark")
            self.theme_status = "dark"
        else:
            self.switch.deselect()  # Switch AUS
            if self.sun_image:
                self.image_label.configure(image=self.sun_image)
            ctk.set_appearance_mode("light")
            self.theme_status = "light"

    def toggle_mode(self):
        if self.switch.get() == 1:
            self.theme_status = "dark"
            ctk.set_appearance_mode("dark")
            if self.moon_image:
                self.image_label.configure(image=self.moon_image)
        else:
            self.theme_status = "light"
            ctk.set_appearance_mode("light")
            if self.sun_image:
                self.image_label.configure(image=self.sun_image)

        self.config.set_config("theme", self.theme_status)