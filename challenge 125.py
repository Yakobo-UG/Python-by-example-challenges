#Create a program that will ask the user to enter a number in a box. When they click on a button it will add that number to a total and display it in another box. This can be repeated as many times as they want and keep adding to the total. There should be another button that resets the total back to 0 and empties the original text box, ready for them to start again.
from tkinter import *
# adding function
def onclick():
    num = text1.get()
    num = int(num)
    add = text2["text"]
    add = int(add)
    Total =  num + add
    text2["text"] = Total

#reseting function
def reset():
    text2["text"] = 0
    text1.delete(0, END)
    text1.focus()


#f2rame 
window = Tk()
window.title("Program")
window.geometry("500x500")


#button
button = Button(text="Press here", command= onclick )
button.place(x = 150, y = 200, width= 200, height= 100)
button["bg"] = "black"
button["fg"] = "white"

#label 
lable = Label(text="Enter number here in the box: ")
lable.place(x = 150, y = 170 )

#user entry
text1 = Entry(text= " ")
text1.place(x= 150, y=100, width= 200, height= 70)
text1["justify"] = "left"
text1.focus()

#user display 
text2 = Message(text=  0)
text2.place(x= 150, y=50, width= 200, height= 40)
text2["bg"] = "yellow"
text2["fg"] = "black"

#reseting buttton
button1 = Button(text="clear", command= reset )
button1.place(x = 200, y = 350, width= 100, height= 50)
button1["bg"] = "blue"
button1["fg"] = "green"



#running the program
mainloop()
