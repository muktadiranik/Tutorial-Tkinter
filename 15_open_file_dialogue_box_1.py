from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.title("title")
root.iconbitmap("icon.ico")
font = "Segoe UI"
img = None

label_1 = Label(root)
label_1.pack()

label_2 = Label(root)
label_2.pack()


def open_file():
    global img, label_1, label_2
    root.file = filedialog.askopenfile(initialdir=".",
                                       filetypes=(("jpg", "*.jpg"),
                                                  ("all", "*.*")))
    img = ImageTk.PhotoImage(Image.open(root.file.name))
    label_1.pack_forget()
    label_1 = Label(root, image=img)
    label_1.pack()

    label_2.pack_forget()
    label_2 = Label(root, text=root.file.name, font=(font, 12))
    label_2.pack()


btn_open = Button(root, text="open", font=(font, 12),
                  command=open_file)
btn_open.pack()

btn_exit = Button(root, text="exit", font=(font, 12),
                  command=root.quit)
btn_exit.pack()

root.mainloop()
