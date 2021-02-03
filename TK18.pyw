# tk18.pwy

import tkinter as tk
def print_txtval():
    val_en = en.get()
    print(val_en)
    en.delete(0,tk.END)

root = tk.Tk()
en = tk.Entry()
en.(0,tk.END)
bt = tk.Button(text = 'Button',command=print_txtval)
[widget.pack() for widget in (en,bt)]
en.focus_set()

root.mainloop()


