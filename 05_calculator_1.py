from tkinter import *

root = Tk()
root.title("calculator")

total = 0.0
operation = None

entry = Entry(root, font=0)
entry.grid(row=0, columnspan=4)

label = Label(root, text="memory")
label.grid(row=6, column=0)

entry_total = Entry(root, font=0)
entry_total.grid(row=6, column=1, columnspan=4)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def button_click(x):
    global total
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(x))
    # entry.insert(END, x)
    entry_total.delete(0, END)
    entry_total.insert(0, total)

def button_dot():
    global total
    a = entry.get()
    if "." in a:
        pass
    elif a is None:
        entry.insert(0, "0.")
    else:
        entry.insert(0, str(a) + ".")

def button_AC():
    global total, operation
    total = 0.0
    operation = None
    entry.delete(0, END)
    entry_total.delete(0, END)
    entry_total.insert(0, total)

def button_add():
    global total, operation
    a = float(entry.get())
    total = add(total, a)
    operation = "+"
    entry.delete(0, END)
    entry_total.delete(0, END)
    entry_total.insert(0, total)

def button_sub():
    global total, operation
    a = float(entry.get())
    total = sub(a, total)
    operation = "-"
    entry.delete(0, END)
    entry_total.delete(0, END)
    entry_total.insert(0, total)

def button_mul():
    global total, operation
    a = float(entry.get())
    total = 1.0
    total = mul(total, a)
    operation = "*"
    entry.delete(0, END)
    entry_total.delete(0, END)
    entry_total.insert(0, total)

def button_div():
    global total, operation
    a = float(entry.get())
    total = 1.0
    total = div(a, total)
    operation = "/"
    entry.delete(0, END)
    entry_total.delete(0, END)
    entry_total.insert(0, total)

def button_equal():
    global total, operation
    a = float(entry.get())
    entry.delete(0, END)
    if operation == "+":
        total = add(total, a)
        entry.insert(0, total)
    if operation == "-":
        total = sub(total, a)
        entry.insert(0, total)
    if operation == "*":
        total = mul(total, a)
        entry.insert(0, total)
    if operation == "/":
        try:
            total = div(total, a)
            entry.insert(0, total)
        except Exception as e:
            entry.insert(0, e)
    total = 0.0
    operation = None
    entry_total.delete(0, END)
    entry_total.insert(0, total)

# button
btn_AC = Button(root, text="C", padx=20, pady=10, border=4, command=button_AC)
btn_div = Button(root, text="/", padx=20, pady=10, border=4, command=button_div)
btn_mul = Button(root, text="*", padx=20, pady=10, border=4, command=button_mul)
btn_sub = Button(root, text="-", padx=20, pady=10, border=4, command=button_sub)
btn_7 = Button(root, text="7", padx=20, pady=10, border=4, command=lambda: button_click(7))
btn_8 = Button(root, text="8", padx=20, pady=10, border=4, command=lambda: button_click(8))
btn_9 = Button(root, text="9", padx=20, pady=10, border=4, command=lambda: button_click(9))
btn_add = Button(root, text="+", padx=20, pady=35, border=4, command=button_add)
btn_4 = Button(root, text="4", padx=20, pady=10, border=4, command=lambda: button_click(4))
btn_5 = Button(root, text="5", padx=20, pady=10, border=4, command=lambda: button_click(5))
btn_6 = Button(root, text="6", padx=20, pady=10, border=4, command=lambda: button_click(6))
btn_1 = Button(root, text="1", padx=20, pady=10, border=4, command=lambda: button_click(1))
btn_2 = Button(root, text="2", padx=20, pady=10, border=4, command=lambda: button_click(2))
btn_3 = Button(root, text="3", padx=20, pady=10, border=4, command=lambda: button_click(3))
btn_equal = Button(root, text="=", padx=20, pady=35, border=4, command=button_equal)
btn_0 = Button(root, text="0", padx=55, pady=10, border=4, command=lambda: button_click(0))
btn_dot = Button(root, text=".", padx=20, pady=10, border=4, command=lambda: button_click("."))

# button on screen
btn_0.grid(row=5, column=0, columnspan=2)
btn_dot.grid(row=5, column=2)
btn_1.grid(row=4, column=0)
btn_2.grid(row=4, column=1)
btn_3.grid(row=4, column=2)
btn_equal.grid(row=4, column=3, rowspan=2)
btn_4.grid(row=3, column=0)
btn_5.grid(row=3, column=1)
btn_6.grid(row=3, column=2)
btn_7.grid(row=2, column=0)
btn_8.grid(row=2, column=1)
btn_9.grid(row=2, column=2)
btn_add.grid(row=2, column=3, rowspan=2)
btn_AC.grid(row=1, column=0)
btn_div.grid(row=1, column=1)
btn_mul.grid(row=1, column=2)
btn_sub.grid(row=1, column=3)

root.mainloop()
