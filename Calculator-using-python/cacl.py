from tkinter import *

window = Tk()
window.minsize(300, 590)
window.title("CALCULATOR")

window.config(background="black")
label = Label(text="", width=20, height=5, background="Black", fg="White")
label.grid(column=0, row=0, columnspan=2)

equation = ""


def number(n):
    global equation
    equation = equation + str(n)
    label.config(text=equation)


def clear():
    global equation
    label.config(text="")
    equation = ""


def enter():
    global equation
    answer = str(eval(equation))
    equation = answer
    label.config(text=answer)


num1 = Button(text="1", background="Black", fg="White", width=17, height=7, command=lambda: number(1))
num1.grid(column=0, row=1)
num2 = Button(text="2", background="Black", fg="White", width=17, height=7, command=lambda: number(2))
num2.grid(column=1, row=1)
num3 = Button(text="3", background="Black", fg="White", width=17, height=7, command=lambda: number(3))
num3.grid(column=2, row=1)
num4 = Button(text="4", background="Black", fg="White", width=17, height=7, command=lambda: number(4))
num4.grid(column=0, row=2)
num5 = Button(text="5", background="Black", fg="White", width=17, height=7, command=lambda: number(5))
num5.grid(column=1, row=2)
num6 = Button(text="6", background="Black", fg="White", width=17, height=7, command=lambda: number(6))
num6.grid(column=2, row=2)
num7 = Button(text="7", background="Black", fg="White", width=17, height=7, command=lambda: number(7))
num7.grid(column=0, row=3)
num8 = Button(text="8", background="Black", fg="White", width=17, height=7, command=lambda: number(8))
num8.grid(column=1, row=3)
num9 = Button(text="9", background="Black", fg="White", width=17, height=7, command=lambda: number(9))
num9.grid(column=2, row=3)
plus = Button(text="+", background="Black", fg="White", width=17, height=7, command=lambda: number("+"))
plus.grid(column=3, row=1)
sub = Button(text="-", background="Black", fg="White", width=17, height=7, command=lambda: number("-"))
sub.grid(column=3, row=2)
div = Button(text="/", background="Black", fg="White", width=17, height=7, command=lambda: number("/"))
div.grid(column=3, row=3)
mult = Button(text="x", background="Black", fg="White", width=17, height=7, command=lambda: number("*"))
mult.grid(column=3, row=4)
enter = Button(text="ENTER", background="Black", fg="White", width=55, height=7, command=enter)
enter.grid(column=0, row=4, columnspan=3)
clear = Button(text="CLEAR", background="Black", fg="White", width=17, height=7, command=clear)
clear.grid(column=3, row=0)
window.mainloop()
