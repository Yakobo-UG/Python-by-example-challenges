#Create a program that will allow the user to create a new .csv file. It should ask them to enter the name and age of a person and then allow them to add this to the end of the file they have just created.
import csv
from os import name
from tkinter import *

def create():
    file = open("newfile.csv", "w")
    file.close()

def add():
    file = open("newfile.csv", "w")
    name = text1.get()
    age = text2.get()
    new = name + ", " + age + "\n",
    file.write(str(new))
    file.close()
    text1.delete(0, END)
    text2.delete(0, END)
    


#frame/ window
window = Tk()
window.geometry("500x500")
window.title("Program")

#lable ask name 
lable = Label(text="Enter  name")
lable.place(x=100, y=170)

#user input name 
text1 = Entry(text=" ")
text1.place(x=100, y=200, width= 100, height= 70)
text1.focus()

#lable ask age
lable1 = Label(text="Enter age")
lable1.place(x=100, y=280)

#user input  age
text2 = Entry(text=" ")
text2.place(x=100, y=300, width= 100, height= 70)


#button for creating the file
button = Button(text="file create", command= create)
button.place(x=100, y=350, width= 100, height= 70 )

#button for creating the file
button = Button(text="add to file", command= add)
button.place(x=100, y=450, width= 100, height= 70)




#running th eprogram
mainloop()

#failed to come out as intended