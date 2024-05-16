import wikipedia
from gtts import gTTS
import os
from tkinter import *

language = "en"
window = Tk()
window.minsize(1000, 550)
window.title("text/speech to speech")
window.config(background="Black")

results = ""


def on_click():
    global results
    wiki = wikipedia.search(str(enter_text.get()))
    wiki_summary = wikipedia.summary(wiki)
    results = str(wiki_summary)
    label.config(text=results)


def on_voice():
    txt_speech = gTTS(text=results, lang=language, slow=False)
    txt_speech.save("output.mp3")
    os.system("output.mp3")


enter_text = Entry(width=40, highlightthickness=0)
enter_text.place(x=5, y=20)

button = Button(text="Generate text", width=20, highlightthickness=0, command=on_click)
button.place(x=5, y=50)
button.config(fg="white", background="grey18")
button1 = Button(text="Generate voice", width=20, highlightthickness=0, command=on_voice)
button1.place(x=5, y=80)
button1.config(fg="white", background="grey18")

label = Label(text="\n", width=100, height=35, highlightthickness=0, wraplength=600, fg="White", background="grey16")
label.place(x=280, y=10)
window.mainloop()
