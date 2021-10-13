#Create a window that will ask the user to enter a number in a text box. When they click on a button it will use the code variable.isdigit() to check to see if it is a whole number. If it is a whole number, add it to a list box, otherwise clear the entry box. Add another button that will clear the list.
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
#list in tkinter
list1 = Listbox()
list1.place(x=200, y= 200, width= 100, height= 70)
#runnning the program
mainloop()