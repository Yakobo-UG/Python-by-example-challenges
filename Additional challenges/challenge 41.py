#Given two strings, first_name and last_name, return a single string in the format "last, first".
FirstName = str(input("ENter your name: "))
SecondName = str(input("Enter your second name: "))
def One(FirstName, SecondName):
    return FirstName + " " + SecondName
print(One(FirstName, SecondName))