import customtkinter as ctk

from PIL import Image

class DarkLightmode(ctk.CTkFrame):  
    def __init__(self, master):
        super().__init__(master)

        # Hintergrund wie Hauptfenster
        self.configure(fg_color=master.cget("fg_color")) 

        # Status-Variable initialisieren
        self.dl_status = "dark"  

        # Bilder laden
        self.sonne_image = ctk.CTkImage(Image.open("./data/img/sunny-outline.png"), size=(32, 32))
        self.mond_image = ctk.CTkImage(Image.open("./data/img/moon-outline.png"), size=(32, 32))

        # Maus Hoverfarbe

        # Image-Label
        self.image_label = ctk.CTkLabel(self, image=self.sonne_image, corner_radius=10, text="")
        self.image_label.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="ne")
        
        # Klick-Event binden
        self.image_label.bind("<Button-1>", self.dark_lightmode)

        # Hover-Event binden
        self.image_label.bind("<Enter>", self.hover_enter)
        self.image_label.bind("<Leave>", self.hover_leave)

    def dark_lightmode(self, event=None):
        if self.dl_status == "dark":
            self.dl_status = "light"
            ctk.set_appearance_mode("light")
            self.image_label.configure(image=self.mond_image)
        else:
            self.dl_status = "dark"
            ctk.set_appearance_mode("dark")
            self.image_label.configure(image=self.sonne_image)

    def hover_enter(self, event):
        if self.dl_status == "dark":
            self.hover_bg = "#333333"
        else:
            self.hover_bg = "#ACACAC"

        self.image_label.configure(fg_color=self.hover_bg)

    def hover_leave(self, event):
        self.default_bg = self.cget("fg_color")
        self.image_label.configure(fg_color=self.default_bg)