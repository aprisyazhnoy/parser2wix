import tk as tkinter


print("module tkinter loaded")

from tkinter import *
from tkinter import ttk

root = Tk()
frm =ttk.Frame(root,padding=10)
frm.grid()
ttk.Label(frm, text="Hello world!").grid(column=0,row=0)
ttk.Button(frm, text="Quit", command = root.destroy).grid(column=1,row=0)

ttk.Button(frm, text="Scan(rescan)").grid(column=0,row=2)

root.mainloop()

