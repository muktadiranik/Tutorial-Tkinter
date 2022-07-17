from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("title")
root.iconbitmap("icon.ico")
font = ("Segoe UI", 16)
i = ImageTk.PhotoImage(Image.open("image.png"))

def button():
    global i
    top = Toplevel()
    Label(top, text="top", font=font).pack()
    Label(top, image=i).pack()
    Button(top, text="destroy", font=font,
           command=top.destroy).pack()

Label(root, image=i).pack()
Button(root, text="button", font=font,
       command=button).pack()




root.mainloop()