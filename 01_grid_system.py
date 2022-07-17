from tkinter import *

root = Tk()

status_1 = Label(root, text="label_1")
label_2 = Label(root, text="label_2")
label_3 = Label(root, text="label_3")
label_4 = Label(root, text="label_4")

status_1.grid(row=0, column=0)
label_2.grid(row=1, column=1)
label_3.grid(row=2, column=2)
label_4.grid(row=3, column=3)

root.mainloop()
