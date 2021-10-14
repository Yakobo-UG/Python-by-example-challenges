#Alter program 128 to add a third button that will save the list to a .csv file. The code  tmp_list = num_list.get(0,END) can be used to save the contents of a list box as tuple called tmp_list. 
import csv
from tkinter import *
#function to run the code
def onclick():
    num = text1.get()
    if num.isdigit():
        list1.insert(END, num)
        text1.delete(0, END)
        text1.focus()
    else:
        text1.delete(0,END)
        text1.focus()
#saves to file 
def tofile():
    file = open("list.csv", "w")
    store= list1.get(0, END)
    item = 0
    for i in store:
        new = store[item] + "\n"
        file.write(new)
        item = item + 1
    file.close()

#window
window = Tk()
window.geometry("500x500")
window.title("Program")
#user input
text1 = Entry(text=" ")
text1.place(x=50, y=100, width= 100, height= 100)
text1["bg"] = "pink"
text1["fg"] = "white"
#button to be clicked
button = Button(text="Press me", command= onclick)
button.place(x= 120, y=200, width=70, height= 70)
#button to save to CSV file
button1 = Button(text="save to file", command= tofile)
button1.place(x= 120, y=300, width=70, height= 70)
#list in tkinter
list1 = Listbox()
list1.place(x=200, y= 200, width= 100, height= 70)
#runnning the program
mainloop()

