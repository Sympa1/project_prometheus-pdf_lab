from gui import Gui
from classes import Utils

def main():
    Utils.write_to_log("test log eintrag")
    app = Gui()
    app.mainloop()

if __name__ == "__main__":
    main()