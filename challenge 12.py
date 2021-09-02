#Ask for two numbers. If the first one is larger than the second, display the second number first and then the first number, otherwise show the first number first and then the second. 

First_No = int(input("Entaer the first number: "))
Second_No = int(input("ENter the second number: "))

if First_No > Second_No: 
    print( Second_No,    First_No   )
else:
    print(First_No,  Second_No)
