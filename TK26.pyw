#tk26.pyw
import tkinter as tk
def get_selpoint():
    sel_start = tk.index('sel.first')
    sel_end = txt.index('sel_last')
    print(tk.get(sel_start,sel_end))

root = tk.Tk()
tx = tk.Text(width=30,height=5)
bt = tk.Button(text='print selected area',command=print_selpoint)
[widget.pack()for widget in (tx,bt)]

root.mainloop()