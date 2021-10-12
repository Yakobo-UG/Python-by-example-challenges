#simple button
from tkinter import *
#button after its pressed
def call():
    msg = Label(window, text= "you pressed the button")
    msg.place(x=20, y=50)
    button["justify"] = "left1"
    button["bg"] = "yellow"
    button["fg"] = "black"

#this is the button before its pressed
window = Tk()
window.geometry("200x200")
button = Button(text= "Press me ", command=call)
button.place(x=30, y=20, width=120, height=25)
window.mainloop()

