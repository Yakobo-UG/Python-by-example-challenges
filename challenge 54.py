#Randomly choose either heads or tails (“h” or “t”). Ask the user to make their choice. If their choice is the same as the randomly selected value, display the message “You win”, otherwise display “Bad luck”. At the end, tell the user if the computer selected heads or tails.
import random
Rand = random.choice(["h","t"])
choice = str(input("Enter your choice: "))
if choice == Rand:
    print("You win")
else:
    print("Bad luck")

print("The computer picked", Rand)
