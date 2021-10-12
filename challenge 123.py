#Create a window that will ask the user to enter their name. When they click on a button it should display the message “Hello” and their name and change the background colour and font colour of the message box. 

from tkinter import *
#after clinked
def onclick():
    name = textbox1.get()
    message = "Hello " + str(name)
    textbox2["bg"] = "blue"
    textbox2["fg"] = "red"
    textbox2["text"] = message
    

#before clicked
#the entire window
window = Tk()
window.title("Name")
window.geometry("500x300")

#lable asking to enter name
lable = Label(text= "Enter your name: ")
lable.place(x=150, y=70)

#box where name will be entered
textbox1 = Entry(text=" ")
textbox1.place(x=150, y=100, width = 100, height= 50)
textbox1["justify"] = "left"
textbox1.focus()

#the button to be pressed
button = Button(text= "Press me", command= onclick)
button.place(x=150, y=170, width=70, height=50)

#where the output will be displayed
textbox2 = Message(text = "")
textbox2.place(width=150, height=50, x = 150, y= 20)
textbox2["justify"] = "center"
textbox2["bg"] = "yellow"
textbox2["fg"] = "black"

#ruunig the code
window.mainloop()
