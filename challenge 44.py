#Ask how many people the user wants to invite to a party. If they enter a number below 10, ask for the names and after each name display “[name] has been invited”. If they enter a number which is 10 or higher, display the message “Too many people”.

people = int(input("Enter the number pf people: "))

if people < 10: 
    for i in range(0, people):
        Names = str(input("Enter your names "))
        print(Names, "you are invited")
else:
    print("Too many people")
