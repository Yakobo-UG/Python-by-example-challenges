#Update program 056 so that it tells the user if they are too high or too low before they pick again
import random
num = random.randint(1,10)
ask = int(input("Enter a random number: "))
while ask != num:
    if ask > num:
        print("Too high, Try agian")
        ask = int(input("Enter a random number: "))
    elif ask < num:
        print("Too low, Try agian")
        ask = int(input("Enter a random number: "))
else:
    print("You found the randowm number", num)