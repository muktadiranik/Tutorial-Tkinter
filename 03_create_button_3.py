from tkinter import *

root = Tk()

btn_1 = Button(root, text="button_1", font=("Arial", 18))
btn_1.pack(side=LEFT)

btn_2 = Button(root, text="button_2", font=("Consolas", 18))
btn_2.pack(side=TOP)

btn_3 = Button(root, text="button_3", font=("Helvetica", 18))
btn_3.pack(side=RIGHT)

root.mainloop()