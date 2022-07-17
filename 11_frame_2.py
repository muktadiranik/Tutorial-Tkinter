from tkinter import *

root = Tk()
root.title("title")
root.iconbitmap("icon.ico")

# frame_1
frame_1 = LabelFrame(root)
frame_1.pack(anchor=N)

btn_1 = Button(frame_1, text="button_1")
btn_1.pack(side=LEFT)

btn_2 = Button(frame_1, text="button_2")
btn_2.pack(side=RIGHT)

# frame_2
frame_2 = LabelFrame(root)
frame_2.pack(anchor=E)

btn_3 = Button(frame_2, text="button_3")
btn_3.pack(side=TOP)

btn_4 = Button(frame_2, text="button_4")
btn_4.pack(side=BOTTOM)





root.mainloop()
