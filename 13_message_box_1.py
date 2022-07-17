import tkinter.messagebox
from tkinter import *

root = Tk()
root.title("title")
root.iconbitmap("icon.ico")

radio_btn_list = [
    ("radio_button_1", "button_1"),
    ("radio_button_2", "button_2"),
    ("radio_button_3", "button_3"),
    ("radio_button_4", "button_4")
]

a = StringVar()
a.set("button_1")

frame_1 = LabelFrame(root, text="frame_1", padx=10, pady=10)
frame_1.pack(padx=10, pady=10, anchor=NW)

for text, value in radio_btn_list:
    Radiobutton(frame_1, text=text, variable=a, value=value,
                command=lambda :radio_select(a.get())).pack()

frame_2 = LabelFrame(root, text="frame_2", padx=10, pady=10)
frame_2.pack(padx=10, pady=10, anchor=NE)

def showinfo():
    tkinter.messagebox.showinfo("messagebox", a.get())

btn_1 = Button(frame_2, text="showinfo", padx=5, pady=5,
               command=showinfo)
btn_1.pack(anchor=CENTER)

def showerror():
    tkinter.messagebox.showerror("messagebox", a.get())

btn_1 = Button(frame_2, text="showerror", padx=5, pady=5,
               command=showerror)
btn_1.pack(anchor=CENTER)

def showwarning():
    tkinter.messagebox.showwarning("messagebox", a.get())

btn_1 = Button(frame_2, text="showwarning", padx=5, pady=5,
               command=showwarning)
btn_1.pack(anchor=CENTER)

def askokcancel():
    tkinter.messagebox.askokcancel("messagebox", a.get())

btn_1 = Button(frame_2, text="askokcancel", padx=5, pady=5,
               command=askokcancel)
btn_1.pack(anchor=CENTER)

def askyesno():
    global status_return, frame_4
    b = tkinter.messagebox.askyesno("messagebox", a.get())
    status_return.pack_forget()
    status_return = Label(frame_4, text=b, relief=SUNKEN, width=10)
    status_return.pack(side=RIGHT)

btn_1 = Button(frame_2, text="askyesno", padx=5, pady=5,
               command=askyesno)
btn_1.pack(anchor=CENTER)

def askquestion():
    tkinter.messagebox.askquestion("messagebox", a.get())

btn_1 = Button(frame_2, text="askquestion", padx=5, pady=5,
               command=askquestion)
btn_1.pack(anchor=CENTER)

def askyesnocancel():
    global status_return, frame_4
    c = tkinter.messagebox.askyesnocancel("messagebox", a.get())
    status_return.pack_forget()
    status_return = Label(frame_4, text=c, relief=SUNKEN, width=10)
    status_return.pack(side=RIGHT)
btn_1 = Button(frame_2, text="askyesnocancel", padx=5, pady=5,
               command=askyesnocancel)
btn_1.pack(anchor=CENTER)

frame_3 = LabelFrame(frame_2)
frame_3.pack()

label_1 = Label(frame_3, text="select: ", width=10)
label_1.pack(side=LEFT)

status_1 = Label(frame_3, text=a.get(), relief=SUNKEN, width=10)
status_1.pack(side=RIGHT)

frame_4 = LabelFrame(frame_2)
frame_4.pack()

label_2 = Label(frame_4, text="return: ", width=10)
label_2.pack(side=LEFT)

status_return = Label(frame_4, text="", relief=SUNKEN, width=10)
status_return.pack(side=RIGHT)

def radio_select(x):
    global status_1
    status_1.pack_forget()
    status_1 = Label(frame_3, text=x, relief=SUNKEN, width=10)
    status_1.pack(side=RIGHT)



root.mainloop()