#sk the user for a list of five integers. Store them in an array. Sort the list and display it in reverse ord
from array import *
num = array("i", [])
for i in range (0,5):
    num1 = int(input("Enter number: "))
    num.append(num1)
num = sorted(num)
num.reverse()
print(num)
