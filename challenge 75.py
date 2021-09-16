#Create a list of four three-digit numbers. Display the list to the user, showing each item from the list on a separate line. Ask the user to enter a three-digit number. If the number they have typed in matches one in the list, display the position of that number in the list, otherwise display the message “That is not in the list”
num =["123", "134", "155", "177" ]
print(num)

for i in num:
    print(i)
digits = int(input("Enter a three digit number: "))

if digits in num:
    index = num.index(digits)
    print(index)
else:
    print("That is not in the list")


    #finised but failed to get it 