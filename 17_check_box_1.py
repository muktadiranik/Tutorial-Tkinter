import tkinter.messagebox
from tkinter import *

root = Tk()
root.title("title")
root.iconbitmap("icon.ico")

a = IntVar()

def check():
    tkinter.messagebox.showinfo("sample", str(a.get()))

check_1 = Checkbutton(root, text="check_1",
                      variable=a)
check_1.pack()

Button(root, text="button_1",
               command=check).pack()

b = StringVar()
def check_StringVar():
    tkinter.messagebox.showinfo("", b.get())

check_2 = Checkbutton(root, text="check_2",
                      variable=b,
                      onvalue="on",
                      offvalue="off")
check_2.deselect()
check_2.pack()
Button(root, text="button_2",
       command=check_StringVar).pack()

root.mainloop()