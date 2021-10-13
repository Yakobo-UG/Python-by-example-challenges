#1 kilometre = 0.6214 miles and 1 mile = 1.6093 kilometres. Using these figures, make a program that will allow the user to convert between miles and kilometres. 
from tkinter import *
def Onkili():
    km = text1.get()
    km = int(km)
    answer = km*0.6214
    text2["text"] = answer

def Onmile():
    ml = text1.get()
    ml = int(ml)
    answer2 = ml*1.6093
    text2["text"] = answer2


#window
window = Tk()
window.geometry("500x500")
window.title("Program")

#lable
lable = Label(text="Enter kilometers or miles")
lable.place(x= 100, y= 100)

#lable 2
lable1 = Label(text="Answers come here: ")
lable1.place(x= 100, y= 255)

#user input
text1 = Entry(text= " ")
text1.place(x = 100, y= 120, width= 150, height= 70)
text1.focus()
text1["justify"] = "center"
text1["bg"] = "Yellow"

#user output
text2 = Message(text= 0)
text2.place(x = 100, y= 280, width= 150, height= 70)
text2["bg"] = "blue"
text2["fg"] = "black"

#button kilometer converter
button1 = Button(text=" to kilometer", command= Onkili)
button1.place(x= 60, y=200, width= 100, height= 50)

#button miles converter
button2 = Button(text=" to miles", command=Onmile)
button2.place(x= 200, y=200, width= 100, height= 50)

#running the program 
mainloop()