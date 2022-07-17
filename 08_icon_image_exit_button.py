from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("title")
root.iconbitmap("icon.ico")

btn_1 = Button(root, text="1")
btn_1.pack(side=LEFT, padx=20)

btn_2 = Button(root, text="2")
btn_2.pack(pady=20)

btn_3 = Button(root, text="3")
btn_3.pack(side=RIGHT, padx=20)

img = ImageTk.PhotoImage(Image.open("image.png"))
label = Label(root, image=img)
label.pack()






btn_exit = Button(root, text="exit", command=root.quit)
btn_exit.pack(pady=20)

root.mainloop()
