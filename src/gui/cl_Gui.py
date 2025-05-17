import customtkinter as ctk

from PIL import Image
from .cl_MyCheckboxFrame import MyCheckboxFrame

class Gui(ctk.CTk):  
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("400x180")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Aktueller Modus
        self.dl_status = "dark"
        ctk.set_appearance_mode(self.dl_status)

        # Bilder laden
        self.sonne_image = ctk.CTkImage(Image.open("./data/img/sunny-outline.png"), size=(32, 32))
        self.mond_image = ctk.CTkImage(Image.open("./data/img/moon-outline.png"), size=(32, 32))

        # Image-Label
        self.image_label = ctk.CTkLabel(self, image=self.mond_image, text="")
        self.image_label.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="ne")

        # Klick-Event binden
        self.image_label.bind("<Button-1>", self.dark_lightmode)

        self.checkbox_frame = MyCheckboxFrame(self)
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")

        self.button = ctk.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    def button_callback(self):
        print("button pressed")
    
    def dark_lightmode(self, event=None):
        if self.dl_status == "dark":
            self.dl_status = "light"
            ctk.set_appearance_mode("light")
            self.image_label.configure(image=self.sonne_image)
        else:
            self.dl_status = "dark"
            ctk.set_appearance_mode("dark")
            self.image_label.configure(image=self.mond_image)