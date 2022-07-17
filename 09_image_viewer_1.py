from tkinter import *
from PIL import Image, ImageTk
import glob

root = Tk()
root.title("image_viewer")
root.iconbitmap("icon.ico")

count = 0
a = glob.glob("**.jpg", recursive=True)
img_list = [ImageTk.PhotoImage(Image.open(i).resize((1280, 720))) for i in a]

label = Label(root, image=img_list[0])
label.grid(row=0, column=1)

label_name = Label(root, text=a[0], font=("Arial", 14))
label_name.grid(row=1, column=1)

label_status = Label(root, text=str(count + 1) + "/" + str(len(img_list)), font=("Arial", 14), relief=SUNKEN, anchor=E)
label_status.grid(row=3, column=1, sticky=W+E)

def btn_prev():
    global count, label, label_name, label_status
    if count > 0:
        count = count - 1
    else:
        count = len(img_list) - 1
    label.grid_forget()
    label_name.grid_forget()
    label = Label(root, image=img_list[count])
    label.grid(row=0, column=1)
    label_name = Label(root, text=a[count], font=("Arial", 14))
    label_name.grid(row=1, column=1)
    label_status.grid_forget()
    label_status = Label(root, text=str(count + 1) + "/" + str(len(img_list)), font=("Arial", 14), relief=SUNKEN, anchor=E)
    label_status.grid(row=3, column=1, sticky=W+E)

def btn_next():
    global count, label, label_name, label_status
    if count < len(img_list) - 1:
        count = count + 1
    else:
        count = 0
    label.grid_forget()
    label_name.grid_forget()
    label = Label(root, image=img_list[count])
    label.grid(row=0, column=1)
    label_name = Label(root, text=a[count], font=("Arial", 14))
    label_name.grid(row=1, column=1)
    label_status.grid_forget()
    label_status = Label(root, text=str(count + 1) + "/" + str(len(img_list)), font=("Arial", 14), relief=SUNKEN, anchor=E)
    label_status.grid(row=3, column=1, sticky=W+E)

btn_prev = Button(root, text="previous", width=10, height=2, font=("Arial", 18), command=btn_prev)
btn_prev.grid(row=0, column=0)

btn_next = Button(root, text="next", width=10, height=2, font=("Arial", 18), command=btn_next)
btn_next.grid(row=0, column=2)

btn_exit = Button(root, text="exit", width=10, font=("Arial", 18), borderwidth=5, command=root.quit)
btn_exit.grid(row=2, column=1)




root.mainloop()