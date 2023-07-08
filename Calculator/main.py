from tkinter import *

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + float(second_number))
    if math == "subtraction":
        e.insert(0, f_num - float(second_number))
    if math == "multiplication":
        e.insert(0, f_num * float(second_number))
    if math == "division":
        e.insert(0, f_num / float(second_number))
    
    
root = Tk()
root.configure(bg='#000')
root.title("Calculator")

e = Entry(root, width=35, borderwidth=6)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

button_1 = Button(root, text="1", padx=40, pady=20, bg="#000", foreground="White", borderwidth=0, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, bg="#000", foreground="White", borderwidth=0, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, bg="#000", foreground="White", borderwidth=0, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, bg="#000", foreground="White", borderwidth=0, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, bg="#000", foreground="White", borderwidth=0, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, bg="#000", foreground="White", borderwidth=0, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, bg="#000", foreground="White", borderwidth=0, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, bg="#000", foreground="White", borderwidth=0, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, bg="#000", foreground="White", borderwidth=0, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, bg="#000", foreground="White", borderwidth=0, command=lambda: button_click(0))
button_dot = Button(root, text=".", padx=40, pady=20, bg="#000", foreground="White", borderwidth=0, command=lambda: button_click('.'))
button_add = Button(root, text="+", padx=40, pady=20, bg="#000", foreground="White", borderwidth=0, command=button_add)
button_subtract = Button(root, text="-", padx=40, pady=20, bg="#000", foreground="White", borderwidth=0, command=button_subtract)
button_multiply = Button(root, text="X", padx=40, pady=20, bg="#000", foreground="White", borderwidth=0, command=button_multiply)
button_divide = Button(root, text="/", padx=40, pady=20, bg="#000", foreground="White", borderwidth=0, command=button_divide)
button_equal = Button(root, text="=", padx=40, pady=20, bg="#000", foreground="White", borderwidth=0, command=button_equal)
button_clear = Button(root, text="Clear", padx=40, pady=20, bg="#000", foreground="White", borderwidth=0, command=button_clear)

def on_enter(e):
    button_0.config(background='blue', foreground= "white")
def on_leave(e):
    button_0.config(background='black', foreground= "white")
button_0.bind('<Enter>', on_enter)
button_0.bind('<Leave>', on_leave)
def on_enter(e):
    button_1.config(background='blue', foreground= "white")
def on_leave(e):
    button_1.config(background='black', foreground= "white")
button_1.bind('<Enter>', on_enter)
button_1.bind('<Leave>', on_leave)
def on_enter(e):
    button_2.config(background='blue', foreground= "white")
def on_leave(e):
    button_2.config(background='black', foreground= "white")
button_2.bind('<Enter>', on_enter)
button_2.bind('<Leave>', on_leave)
def on_enter(e):
    button_3.config(background='blue', foreground= "white")
def on_leave(e):
    button_3.config(background='black', foreground= "white")
button_3.bind('<Enter>', on_enter)
button_3.bind('<Leave>', on_leave)
def on_enter(e):
    button_4.config(background='blue', foreground= "white")
def on_leave(e):
    button_4.config(background='black', foreground= "white")
button_4.bind('<Enter>', on_enter)
button_4.bind('<Leave>', on_leave)
def on_enter(e):
    button_5.config(background='blue', foreground= "white")
def on_leave(e):
    button_5.config(background='black', foreground= "white")
button_5.bind('<Enter>', on_enter)
button_5.bind('<Leave>', on_leave)
def on_enter(e):
    button_6.config(background='blue', foreground= "white")
def on_leave(e):
    button_6.config(background='black', foreground= "white")
button_6.bind('<Enter>', on_enter)
button_6.bind('<Leave>', on_leave)
def on_enter(e):
    button_7.config(background='blue', foreground= "white")
def on_leave(e):
    button_7.config(background='black', foreground= "white")
button_7.bind('<Enter>', on_enter)
button_7.bind('<Leave>', on_leave)
def on_enter(e):
    button_8.config(background='blue', foreground= "white")
def on_leave(e):
    button_8.config(background='black', foreground= "white")
button_8.bind('<Enter>', on_enter)
button_8.bind('<Leave>', on_leave)
def on_enter(e):
    button_9.config(background='blue', foreground= "white")
def on_leave(e):
    button_9.config(background='black', foreground= "white")
button_9.bind('<Enter>', on_enter)
button_9.bind('<Leave>', on_leave)
def on_enter(e):
    button_dot.config(background='blue', foreground= "white")
def on_leave(e):
    button_dot.config(background='black', foreground= "white")
button_dot.bind('<Enter>', on_enter)
button_dot.bind('<Leave>', on_leave)
def on_enter(e):
    button_clear.config(background='orange', foreground= "black")
def on_leave(e):
    button_clear.config(background='black', foreground= "white")
button_clear.bind('<Enter>', on_enter)
button_clear.bind('<Leave>', on_leave)
def on_enter(e):
    button_add.config(background='orange', foreground= "black")
def on_leave(e):
    button_add.config(background='black', foreground= "white")
button_add.bind('<Enter>', on_enter)
button_add.bind('<Leave>', on_leave)
def on_enter(e):
    button_subtract.config(background='orange', foreground= "black")
def on_leave(e):
    button_subtract.config(background='black', foreground= "white")
button_subtract.bind('<Enter>', on_enter)
button_subtract.bind('<Leave>', on_leave)
def on_enter(e):
    button_multiply.config(background='orange', foreground= "black")
def on_leave(e):
    button_multiply.config(background='black', foreground= "white")
button_multiply.bind('<Enter>', on_enter)
button_multiply.bind('<Leave>', on_leave)
def on_enter(e):
    button_divide.config(background='orange', foreground= "black")
def on_leave(e):
    button_divide.config(background='black', foreground= "white")
button_divide.bind('<Enter>', on_enter)
button_divide.bind('<Leave>', on_leave)
def on_enter(e):
    button_equal.config(background='orange', foreground= "black")
def on_leave(e):
    button_equal.config(background='black', foreground= "white")
button_equal.bind('<Enter>', on_enter)
button_equal.bind('<Leave>', on_leave)


button_clear.grid(row=0, column=3)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_divide.grid(row=2, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_multiply.grid(row=3, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_subtract.grid(row=4, column=3)

button_dot.grid(row=5,column=0)
button_0.grid(row=5, column=1)
button_equal.grid(row=5, column=2)
button_add.grid(row=5, column=3)

root.mainloop()
