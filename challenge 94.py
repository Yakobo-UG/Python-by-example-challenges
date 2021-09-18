#Display an array of five numbers. Ask the user to select one of the numbers. Once they have selected a number, display the position of that item in the array. If they enter something that is not in the array, ask them to try again until they select a relevant item.  
from array import *
num = array("i", [1,2,3,4,5])
print(num)
for i in num:
    if i in num:
        try:
            select = int(input("Enter your numbers: "))
            position = num.index(select)
            print(position)
        except:
            print("Try agian")
            select = int(input("Enter your numbers: "))

        
    

