#Ask the user to enter a number between 10 and 20 (inclusive). If they enter a number within this range, display the message “Thank you”, otherwise display the message “Incorrect answer”

Enter_No = int(input("Enter number here: "))
if Enter_No in range(10, 21):
    print("Thank you")
else:
    print("Incorrect answer")