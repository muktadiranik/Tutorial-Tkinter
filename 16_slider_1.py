from tkinter import *

root = Tk()
root.title("title")
root.iconbitmap("icon.ico")

label_1 = Label(root, text="horizontal: 0")
label_1.pack(side=LEFT)

label_2 = Label(root, text="vertical: 0")
label_2.pack(side=LEFT)


def slider_vertical(x):
    global label_1
    label_1.pack_forget()
    label_1 = Label(root, text="vertical: " + str(x))
    label_1.pack(side=LEFT)

def slider_horizontal(y):
    global label_2
    label_2.pack_forget()
    label_2 = Label(root, text="horizontal: " + str(y))
    label_2.pack(side=LEFT)


vertical = Scale(root, from_=0, to=500,
                 command=slider_vertical)
vertical.pack(side=RIGHT)

horizontal = Scale(root, from_=0, to=500, orient=HORIZONTAL,
                   command=slider_horizontal)
horizontal.pack(side=BOTTOM)

root.mainloop()
