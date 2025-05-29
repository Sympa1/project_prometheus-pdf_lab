from tkinter import messagebox

class Messagebox:
    def __init__(self, title, message):
        self.title = title
        self.message = message

    def messagebox_warning(self):
        messagebox.showwarning(self.title, self.message)

    def messagebox_error(self):
        messagebox.showerror(self.title, self.message)

    def messagebox_info(self):
        messagebox.showinfo(self.title, self.message)
