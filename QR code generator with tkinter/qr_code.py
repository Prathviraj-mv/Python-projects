from tkinter import *
import qrcode
import random

window = Tk()
window.title("QR code Generator")
window.minsize(width=500, height=400)
window.config(padx=20, pady=20)

link_enter = Entry(width=30, highlightthickness=0)
link_enter.grid(column=0, row=0)


def gen():
    x = str(random.randint(1, 10000000))
    file_name = x + ".png"
    code = qrcode.make(link_enter.get())
    code.save(file_name)
    qr = PhotoImage(file=file_name)
    qr_label.config(image=qr)
    qr_label.image = qr


button = Button(text="Generate qr code", width=20, command=gen)
button.grid(column=0, row=1)

qr_label = Label(window)
qr_label.config(padx=10)
qr_label.grid(column=1, row=0)

window.mainloop()
