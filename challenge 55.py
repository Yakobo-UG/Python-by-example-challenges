#Randomly choose a number between 1 and 5. Ask the user to pick a number. If they guess correctly, display the message “Well done”, otherwise tell them if they are too high or too low and ask them to pick a second number. If they guess correctly on their second guess, display “Correct”, otherwise display “You lose”.
import random
num = random.randint(1,5)
pick = int(input("Pick anumber: "))
if pick == num:
    print("Well done")
else:
    if pick > num:
        print("Too high")
        pick2 = int(input("Pick a second anumber: "))
    elif pick < num:
        print("Too low")
        pick2 = int(input("Picka second anumber: "))
    if pick2 == num:
        print("correct")
    else:
        print("You lose")