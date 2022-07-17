from tkinter import *

root = Tk()

def get_entry():
    label = Label(root, text=entry.get())
    label.pack()

entry = Entry(root,
              width=50,
              border=2,
              borderwidth=2,
              foreground="black",
              background="white",
              font=0)
entry.pack()
entry.insert(0, "insert")

btn = Button(root, text="get_entry", command=get_entry)
btn.pack()

root.mainloop()