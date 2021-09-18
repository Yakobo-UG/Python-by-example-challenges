#Ask the user to enter numbers. If they enter a number between 10 and 20, save it in the array, otherwise display the message “Outside the range”. Once five numbers have been successfully added, display the message “Thank you” and display the array with each item shown on a separate line. 
from array import *


Newarray = array("i", [])

while len(Newarray) < 5:
    num = int(input("Enter number: "))
    Newarray.append(num)
    if num>=10 and num <=20: 
        print("Thank you")
    else:
        print("Outside the range")
for i in Newarray:
    print(i)

    #failed this one


