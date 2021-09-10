#Ask the user to enter a number. Keep asking until they enter a value over 5 and then display the message “The last number you entered was a [number]” and stop the program
num = int(input("Enter number: "))
while num < 5:
    num = int(input("Enter number: "))
    if num > 5: 
        print ("The last number you enter  was ", num)