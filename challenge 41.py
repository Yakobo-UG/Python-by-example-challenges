#Ask the user to enter their name and a number. If the number is less than 10, then display their name that number of times; otherwise display the message “Too high” three times. 

Name = str(input("ENter name: "))
Num = int(input("Enter number: "))
if Num < 10:
    for i in range(Num):
        print(Name)
else:
    print("Too high")