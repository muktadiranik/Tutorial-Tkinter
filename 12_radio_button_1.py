from tkinter import *

root = Tk()
root.title("title")
root.iconbitmap("icon.ico")

frame_1 = LabelFrame(root, text="frame_1", padx=5, pady=5)
frame_1.pack(padx=5, pady=5, anchor=N)

a = IntVar()
a.set(1)

radio_1 = Radiobutton(frame_1, text="radio_button_1", variable=a, value=1,
                      command=lambda: radio_select(1))
radio_1.pack()

radio_2 = Radiobutton(frame_1, text="radio_button_2", variable=a, value=2,
                      command=lambda: radio_select(2))
radio_2.pack()

frame_2 = LabelFrame(root, text="frame_2", padx=5, pady=5)
frame_2.pack(padx=5, pady=5, anchor=W)

status_1 = Label(frame_2, text=a.get())
status_1.pack()


def radio_select(x):
    global status_1
    label_1.pack_forget()
    label_1 = Label(frame_2, text=a.get())
    label_1.pack()


root.mainloop()
