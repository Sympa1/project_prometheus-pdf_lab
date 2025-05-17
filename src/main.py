from gui import Gui
# Alternativ: from mein_package import Gui (wenn in __init__.py exportiert)

def main():
    app = Gui()
    app.mainloop()

if __name__ == "__main__":
    main()