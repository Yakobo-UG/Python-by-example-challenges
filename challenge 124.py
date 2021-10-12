#Write a program that can be used instead of rolling a six-sided die in a board game.When the user clicks a button it should display a random whole number between 1 to 6 (inclusive).
import random
from tkinter import *
def onclick():
    change = random.randint(1,6)
    enrty["text"] = change

#frame
window = Tk()
window.title("dice game")
window.geometry("500x500")

#button when pressed
button = Button(text="Click to get number", command= onclick )
button.place(x=155, y=200, width=150, height=70)

#where the number will be displayed
enrty = Message(text=" ")
enrty.place(x = 170, y= 100, width= 120, height= 90)
enrty["bg"] = "yellow"
enrty["fg"] = "blue"


mainloop()
