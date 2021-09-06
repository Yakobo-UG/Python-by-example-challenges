#Ask which direction the user wants to count (up or down). If they select up, then ask them for the top number and then count from 1 to that number. If they select down, ask them to enter a number below 20 and then count down from 20 to that number. If they entered something other than up or down, display the message “I don’t understand”

direction = str(input("What direction do you want, up or down?: "))
if direction == "up" or "UP" or "Up":
    Top = int(input("Enter your highest number: "))
    for i in range(1, Top+1):
        print(i)
elif direction == "down" or "DOWN" or "Down":
    below = int(input("Enter your number below 20: "))
    for i in range(20, below, -1):
        print(i)
else:
    print("i dont understand")


#failed to do this challenge 