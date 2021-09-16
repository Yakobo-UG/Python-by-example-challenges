#Ask the user to enter their first name and then display the length of their first name. Then ask for their surname and display the length of their surname. Join their first name and surname together with a space between and display the result. Finally, display the length of their full name (including the space).

FirstName =str(input("ENter your first name: "))
print(len(FirstName))
Surname = str(input("Enter your Surname: "))
print(len(Surname))

join = FirstName +" "+ Surname
print(join)
print(len(join))