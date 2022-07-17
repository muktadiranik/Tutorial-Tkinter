from tkinter import *

root = Tk()
root.title("title")
root.iconbitmap("icon.ico")

frame_1 = LabelFrame(root, text="label_frame_1", padx=5, pady=5)
frame_1.pack(padx=5, pady=5, side=LEFT)

btn_1 = Button(frame_1, text="button_1")
btn_1.pack()

frame_2 = LabelFrame(root, text="label_frame_2", padx=5, pady=5)
frame_2.pack(padx=5, pady=5, side=RIGHT)

btn_2 = Button(frame_2, text="button_2")
btn_2.pack()

frame_3 = LabelFrame(root, text="label_frame_3", padx=5, pady=5)
frame_3.pack(padx=5, pady=5, side=TOP)

btn_3 = Button(frame_3, text="button_3")
btn_3.pack()

frame_4 = LabelFrame(root, text="label_frame_4", padx=5, pady=5)
frame_4.pack(padx=5, pady=5, side=BOTTOM)

btn_4 = Button(frame_4, text="button_4")
btn_4.pack()


root.mainloop()