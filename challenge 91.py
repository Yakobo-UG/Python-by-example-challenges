#Create an array which contains five numbers (two of which should be repeated). Display the whole array to the user. Ask the user to enter one of the numbers from the array and then display a message saying how many times that number appears in the list.  `
from array import *
arr = array("i", [1,2,44,44,6])
print(arr)
num = int(input("Enter one of the numbers from the array: "))
counting = arr.count(num)
print(num ,"appears", counting, "number of times")


