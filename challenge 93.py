#Ask the user to enter five numbers. Sort them into order and present them to the user. Ask them to select one of the numbers. Remove it from the original array and save it in a new array
from array import array

new = array("i", [])
numarray = array("i",[])
for i in range(0,5):
    num =  int(input("Enter number: "))
    numarray.append(num)
numarray = sorted(numarray)
print(numarray)
remove = int(input("Enter number to be removed: "))
numarray.remove(remove)
new.append(remove)
print(new)
print(numarray)
    