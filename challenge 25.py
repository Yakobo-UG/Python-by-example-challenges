#Ask the user to enter their first name. If the length of their first name is under five characters, ask them to enter their surname and join them together (without a space) and display the name in upper case. If the length of the first name is five or more characters, display their first name in lower case. 

first_name = str(input("Enter your first name: "))

if len(first_name) < 5:
    surname = str(input("Enter surname: "))
    print ( first_name.upper() + surname.upper())
    
else:
    print( first_name.lower() + surname.upper())
