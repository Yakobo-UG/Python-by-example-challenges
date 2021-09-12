#Randomly pick a whole number between 1 and 10. Ask the user to enter a number and keep entering numbers until they enter the number that was randomly picked.
import random
num = random.randint(1,10)
ask = int(input("Enter a random number: "))
while ask != num:
    ask = int(input("Enter a random number: "))
else:
    print("You found the randowm number", num)