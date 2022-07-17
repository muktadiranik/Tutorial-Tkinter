from tkinter import *

root = Tk()

def click():
    label = Label(root, text="click")
    label.pack()

button_1 = Button(root, text="button_1")
button_1.pack()

button_2 = Button(root, text="button_2", state=DISABLED)
button_2.pack()

button_3 = Button(root, text="button_3", padx=10, pady=10)
button_3.pack()

button_4 = Button(root, text="click", command=click)
button_4.pack()

button_5 = Button(root, text="click", foreground="white", background="black", borderwidth=5, border=5)
button_5.pack()

root.mainloop()
