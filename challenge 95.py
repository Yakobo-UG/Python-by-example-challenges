#Create an array of five numbers between 10 and 100 which each have two decimal places. Ask the user to enter a whole number between 2 and 5. If they enter something outside of that range, display a suitable error message and ask them to try again until they enter a valid amount. Divide each of the numbers in the array by the number the user entered and display the answers shown to two decimal places.

from array import *
import math
num = array("f",[23.34,54.55,11.23,55.78,76.76])
whole = float(input("Enter whole number between 2 and 5: "))
while whole<2 or whole>5:
    print("Error beyomg range")
    whole = int(input("Enter whole number between 2 and 5: "))
        
else:
    count = num[1]/whole
    rod = round(count,2)
    print(rod)
        

