import customtkinter as ctk

# Übersicht der wichtigsten CustomTkinter GUI-Elemente (Widgets)

root = ctk.CTk()
frame = ctk.CTkFrame(root)
frame.pack(padx=10, pady=10)

# Label
label = ctk.CTkLabel(frame, text="Label")
label.pack(pady=5)

# Button
button = ctk.CTkButton(frame, text="Button")
button.pack(pady=5)

# Entry (Eingabefeld)
entry = ctk.CTkEntry(frame)
entry.pack(pady=5)

# Checkbox
checkbox = ctk.CTkCheckBox(frame, text="Checkbox")
checkbox.pack(pady=5)

# Radiobutton
radiobutton = ctk.CTkRadioButton(frame, text="Radiobutton")
radiobutton.pack(pady=5)

# Switch (Schalter)
switch = ctk.CTkSwitch(frame, text="Switch")
switch.pack(pady=5)

# Slider
slider = ctk.CTkSlider(frame, from_=0, to=100)
slider.pack(pady=5)

# Progressbar
progressbar = ctk.CTkProgressBar(frame)
progressbar.pack(pady=5)
progressbar.set(0.5)  # 50%

# Combobox (Dropdown)
combobox = ctk.CTkComboBox(frame, values=["Option 1", "Option 2", "Option 3"])
combobox.pack(pady=5)

# OptionMenu
optionmenu = ctk.CTkOptionMenu(frame, values=["A", "B", "C"])
optionmenu.pack(pady=5)

# Tabview (Tabs)
tabview = ctk.CTkTabview(frame)
tabview.pack(pady=5)
tabview.add("Tab 1")
tabview.add("Tab 2")

# Scrollbar
scrollbar = ctk.CTkScrollbar(frame)
scrollbar.pack(pady=5)

# Textbox
textbox = ctk.CTkTextbox(frame, width=200, height=50)
textbox.pack(pady=5)

# Segmented Button
segmented_button = ctk.CTkSegmentedButton(frame, values=["One", "Two", "Three"])
segmented_button.pack(pady=5)

# Scrollable Frame
scrollable_frame = ctk.CTkScrollableFrame(frame, width=200, height=80)
scrollable_frame.pack(pady=5)
for i in range(5):
    ctk.CTkLabel(scrollable_frame, text=f"Item {i+1}").pack()

# Tableview (ab CustomTkinter 5.x, ggf. nicht in allen Versionen verfügbar)
try:
    tableview = ctk.CTkTable(frame, row=3, column=2)
    tableview.pack(pady=5)
    tableview.insert(0, 0, "A1")
    tableview.insert(0, 1, "B1")
    tableview.insert(1, 0, "A2")
    tableview.insert(1, 1, "B2")
except AttributeError:
    ctk.CTkLabel(frame, text="CTkTable nicht verfügbar in dieser Version").pack(pady=5)

# Image (als Label)
# img = ctk.CTkImage(...)  # siehe Doku

# InputDialog (CustomTkinter bietet ab v5.x einen einfachen InputDialog)
def open_input_dialog():
    dialog = ctk.CTkInputDialog(text="Bitte gib etwas ein:", title="InputDialog")
    print("Eingabe:", dialog.get_input())

input_button = ctk.CTkButton(frame, text="InputDialog öffnen", command=open_input_dialog)
input_button.pack(pady=5)

# Toplevel-Fenster mit Progressbar
def open_toplevel():
    toplevel = ctk.CTkToplevel(root)
    toplevel.title("Toplevel mit Progressbar")
    toplevel.geometry("300x100")
    label = ctk.CTkLabel(toplevel, text="Fortschritt:")
    label.pack(pady=(20, 5))
    progress = ctk.CTkProgressBar(toplevel)
    progress.pack(pady=5, padx=20, fill="x")
    progress.set(0.7)  # Beispielwert 70%

toplevel_button = ctk.CTkButton(frame, text="Toplevel mit Progressbar", command=open_toplevel)
toplevel_button.pack(pady=5)

root.mainloop()