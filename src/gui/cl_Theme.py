import customtkinter as ctk
from PIL import Image

class Theme(ctk.CTkFrame):  
    def __init__(self, master):
        super().__init__(master)

        # Hintergrund wie Hauptfenster
        self.configure(fg_color=master.cget("fg_color")) 

        # Status-Variable initialisieren
        self.theme_status = "dark"  

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
        self.image_label = ctk.CTkLabel(self.inner_frame, image=self.moon_image, text="")
        self.image_label.place(x=45, y=0)
        self.switch.select()

    def toggle_mode(self):
        if self.switch.get() == 1:
            self.theme_status = "dark"
            ctk.set_appearance_mode("dark")
            self.image_label.configure(image=self.moon_image)
        else:
            self.theme_status = "light"
            ctk.set_appearance_mode("light")
            self.image_label.configure(image=self.sun_image)