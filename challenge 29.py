#Ask the user to enter an integer that is over 500. Work out the square root of that number and display it to two decimal places. 
import math
over = float(input("Enter number over 500: "))
sqr = math.sqrt(over)
if over < 500:
    print("Its not over 500")
else:
    print(round(sqr, 2))
