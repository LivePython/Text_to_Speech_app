from gtts import gTTS
import os
from tkinter import *


def make_to_speach():
    data = entry.get()
    output = gTTS(text=data, lang='en', slow=False)
    output.save('sound.mp3')

    os.system('start sound.mp3')
    entry.delete(0,END)


window = Tk()

window.title("Text-To-Speech")
window.resizable(width=False, height=False)

canvas = Canvas(window, width=400, height=300)
canvas.pack()

heading = Label(text="Text-To-Speach App")
canvas.create_window(200, 50, window=heading)

entry = Entry(window, width=50)
canvas.create_window(200, 100, window=entry)

speach_button = Button(text='Convert To Speech', command=make_to_speach)
canvas.create_window(200, 130, window=speach_button)


window.mainloop()