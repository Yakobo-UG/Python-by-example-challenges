#Add to program 069 to ask the user to enter a number and display the country in that position
Names = ("Uganda","Kenya","Tanzania","Rwanda","Ethiopia")
print(Names)
user = str(input("Enter one of the countries seen above: "))
print(Names.index(user))
num = int(input("Enter index number: "))
print(Names[num])