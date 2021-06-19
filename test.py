from tkinter import ttk
from tkinter import *
root = Tk()
root.geometry("400x400")
diction = {'M': 9, 'Z': 3, 'R': 12}
combo = ttk.Combobox(root, values=tuple(diction.keys()))
combo.bind("<<ComboboxSelected>>", _onSelected)
def _onSelected():
    key = diction.keys()
    if key == "M":
        generate("<<ComboboxSelectedValue-M>>")
def onSelected(event):
    if isinstance:
        key = diction.keys()
        print("{} was selected".format(key))
combo.place(relx=0.2, rely=0.2)

root.mainloop()
