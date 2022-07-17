from tkinter import *
root = Tk()
root.title("title")
root.iconbitmap("icon.ico")

frame_1 = LabelFrame(root, text="radio_button", padx=10, pady=10)
frame_1.pack(padx=10, pady=10, side=LEFT)

radio_btn_list = [
    ("radio_button_1", "button_1"),
    ("radio_button_2", "button_2"),
    ("radio_button_3", "button_3"),
    ("radio_button_4", "button_4")
]

a = StringVar()
a.set("button_1")

for text, value in radio_btn_list:
    Radiobutton(frame_1, text=text, variable=a, value=value,
                command=lambda : radio_select(a.get())).pack()

frame_2 = LabelFrame(root, text="label", padx=10, pady=10)
frame_2.pack(padx=10, pady=10, side=RIGHT)

status_1 = Label(frame_2, text="select: ")
status_1.pack(side=LEFT)

status_1 = Label(frame_2, text=a.get(), relief=SUNKEN)
status_1.pack(side=RIGHT)

def radio_select(x):
    global status_1
    label_1.pack_forget()
    label_1 = Label(frame_2, text=x, relief=SUNKEN)
    label_1.pack(side=RIGHT)



root.mainloop()