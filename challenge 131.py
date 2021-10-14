#Using the .csv file you created for the last challenge, create a program that will allow people to add names and ages to the list and create a button that will display the f the .csv file by importing it to a list box. 

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

def read():
    list1.delete(0, END)
    file = list(csv.reader(open("newfile.csv")))
    tmp = []
    for i in file:
        tmp.append(i)
    x= 0
    for i in tmp:
        data = tmp[x]
        list1.insert(END, data)
        x = x + 1

    


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
button1 = Button(text="add to file", command= add)
button1.place(x=100, y=450, width= 100, height= 70)

#button for displaying
button3 = Button(text="Dispaly", command=read)
button3.place(x=70, y=230, width= 100, height= 50)


#list 
list1 = Listbox()
list1.place(x=50, y=70, width=200, height= 100)

#running th eprogram
mainloop()