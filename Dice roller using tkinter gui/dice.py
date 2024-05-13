from tkinter import *
from PIL import ImageTk, Image
import random

window = Tk()
window.minsize(400, 400)
window.title("DICE ROLL")
window.config(bg="gray13")

# Create images
image1 = ImageTk.PhotoImage(Image.open("images/n1.png"))
image2 = ImageTk.PhotoImage(Image.open("images/n2.png"))
image3 = ImageTk.PhotoImage(Image.open("images/n3.png"))
image4 = ImageTk.PhotoImage(Image.open("images/n4.png"))
image5 = ImageTk.PhotoImage(Image.open("images/n5.png"))
image6 = ImageTk.PhotoImage(Image.open("images/n6.png"))
images = [image5, image4, image6, image1, image3, image2]


def random_image():
    img = random.choice(images)
    dice = Label(image=img, bg="grey9", highlightthickness=0)
    dice.grid(column=0, row=0)
    if img == image1:
        label1.config(text="1")
    if img == image2:
        label1.config(text="2")
    if img == image3:
        label1.config(text="3")
    if img == image4:
        label1.config(text="4")
    if img == image5:
        label1.config(text="5")
    if img == image6:
        label1.config(text="6")


label = Label(window, height=30, width=70, bg="gray9")
label.grid(column=0, row=0)

button = Button(text="ROLL", command=random_image, width=14, highlightthickness=0, bg="Black")
button.config(font=("Arial" , 10), fg="White")
button.grid(column=1, row=1)

label1 = Label(text="0", height=7, width=7, bg="gray9")
label1.config(font=("Arial", 20), fg="White")
label1.grid(column=1, row=0)

window.mainloop()
