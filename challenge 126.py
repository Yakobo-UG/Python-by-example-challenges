#Create a window that will ask the user to enter a name in a text box. When they click on a button it will add it to the end of the list that is displayed on the screen. Create another button which will clear the list. 
from tkinter import *
#appending to the user input
def onclick():
    num = text1.get()
    add = text2["text"]
    together = num + add
    text2["text"] = together

#clearing 
def clear():
    text2["text"] = " "
    text1.delete(0, END)
    text1.focus()

#tkinter window
window = Tk()
window.title("Program")
window.geometry("500x500")

#lebel
lable = Label(text = "ENter your name below: ")
lable.place(x= 60, y= 70)

#user input
text1 = Entry(text= " ")
text1.place(width= 150, height= 100, x= 150, y=150)
text1["justify"] = "left"
text1.focus()

#user display
text2 = Message(text=" ")
text2.place(x=200, y=100, width= 100, height= 30)
text2["bg"] = "yellow"
text2["fg"] = "black"

#button to be clicked
button = Button(text="Press me", command= onclick)
button.place(x=100, y=100, width= 70, height= 50)

#clear button
button1 = Button(text="clear", command= clear)
button1.place(x=250, y=150, width= 70, height= 50)

#running the program
mainloop()