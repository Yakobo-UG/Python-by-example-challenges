#Create an array which will store a list of integers. Generate five random numbers and store them in the array. Display the array (showing each item on a separate line).

from array import *
import random
num = array("i", [])
for i in range(0, 5):
    num1 = random.randint(1,1000)
    num.append(num1)
    num = sorted(num)
    print(num)
    for p in num:
        print(p)
