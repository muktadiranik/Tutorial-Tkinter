from tkinter import *

root = Tk()
root.title("button")

btn = Button(root,
             text="button",
             padx=20,
             pady=10,
             borderwidth=10,
             border=10,
             activebackground="black",
             activeforeground="white",
             background="white",
             foreground="black",)
btn.pack()

root.mainloop()
