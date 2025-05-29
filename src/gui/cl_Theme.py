import customtkinter as ctk
from PIL import Image
from classes import Utils

class Theme(ctk.CTkFrame):  
    def __init__(self, master, config):
        super().__init__(master)
        self.config = config

        # Hintergrund wie Hauptfenster
        self.configure(fg_color=master.cget("fg_color")) 

        # Bilder laden
        self.sun_image = ctk.CTkImage(Image.open("./data/img/sunny-outline.png"), size=(32, 32))
        self.moon_image = ctk.CTkImage(Image.open("./data/img/moon-outline.png"), size=(32, 32))

        # Inner Frame ohne Dehnung
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
            self.image_label.configure(image=self.moon_image)
            ctk.set_appearance_mode("dark")
            self.theme_status = "dark"
        else:
            self.switch.deselect()  # Switch AUS
            self.image_label.configure(image=self.sun_image)
            ctk.set_appearance_mode("light")
            self.theme_status = "light"

    def toggle_mode(self):
        if self.switch.get() == 1:
            self.theme_status = "dark"
            ctk.set_appearance_mode("dark")
            self.image_label.configure(image=self.moon_image)
        else:
            self.theme_status = "light"
            ctk.set_appearance_mode("light")
            self.image_label.configure(image=self.sun_image)

        self.config.set_config("theme", self.theme_status)