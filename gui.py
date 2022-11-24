import tk as tkinter


print("module tkinter loaded")

from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )

root = Tk()
root.title('Parser Wix')
root.geometry('320x240')


frm =ttk.Frame(root,padding=10)
frm.grid()
ttk.Label(frm, text="Hello world!").grid(column=0,row=0)
ttk.Label(frm, text="column1row0").grid(column=1,row=0)

ttk.Button(frm, text="Quit", command = root.destroy).grid(column=1,row=2)

ttk.Button(frm, text="Scan(rescan)").grid(column=0,row=2)
##GET FROM https://www.pythontutorial.net/tkinter/tkinter-open-file-dialog/
open_button = ttk.Button(
    frm,
    text='Open a File',
    command=select_file
).grid(column=0,row=3)
##open_button.pack(expand=True)
##tkinter.filedialog.askopenfile(mode='r', **options)

root.mainloop()

