#Ask the user to enter a number and then enter another number. Add these two numbers together and then ask if they want to add another number. If they enter “y", ask them to enter another number and keep adding numbers until they do not answer “y”. Once the loop has stopped, display the total. 
num1 = int(input("Enter number: "))
add = num1
repeat = "y"
while repeat == "y": 
    num2 = int(input("Enter nunmber: "))
    add = add + num2
    repeat = str(input("Do you want to enter anther number ?: "))
print(add)




