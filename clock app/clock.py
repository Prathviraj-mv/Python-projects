from tkinter import *
import time

window = Tk()
window.title("-----CLOCK-----")
window.minsize(400, 200)
window.config(background="Black")


def time_now():
    current_time = time.strftime('%H:%M:%S')
    day = time.strftime('%d/%m/%Y')

    label.config(text=current_time)
    label1.config(text=day)

    label.after(1000, time_now)
    label1.after(1000, time_now)


label = Label(window, background="Black", fg="White", highlightthickness=0, font=("arial", 80, "bold"))
label.grid(row=0, column=0)
label1 = Label(window, background="Black", fg="White", highlightthickness=0, font=("arial", 20, "bold"))
label1.grid(row=1, column=0)

time_now()

window.mainloop()
