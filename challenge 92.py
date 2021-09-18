#Create two arrays (one containing three numbers that the user enters and one containing a set of five random numbers). Join these two arrays together into one large array. Sort this large array and display it so that each number appears on a separate line.
import random
from array import *
userarray = array("i",[])
randarrary = array("i",[])

for i in range(0,3):
    num = int(input("Enter numbers: "))
    userarray.append(num)

for p in range(0,5):
    num1 = random.randint(1,10)
    randarrary.append(num1)

userarray.extend(randarrary)
userarray = sorted(userarray)
for z in userarray:
    print(z)
