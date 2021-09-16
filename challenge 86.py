#Ask the user to enter a new password. Ask them to enter it again. If the two passwords match, display “Thank you”. If the letters are correct but in the wrong case, display the message “They must be in the same case”, otherwise display the message “Incorrect”

newpass =str(input("Enter new passward: "))
newpass1 = str(input("Enter new passward: "))
if newpass == newpass1:
    print("Thank you")
elif newpass.lower() == newpass1.lower():
        print("They must be in the same case")
else:
    print("Incorrect")