#Create a variable called compnum and set the value to 50. Ask the user to enter a number. While their guess is not the same as the compnum value, tell them if their guess is too low or too high and ask them to have another guess. If they enter the same value as compnum, display the message “Well done, you took [count] attempts”.

compnum = 50
guess = int(input("Enter number here: "))
count = 0

while guess != compnum:
    if guess > compnum:
        print("guess is too high")
    else:
        print("guess is to low")
    count = count + 1
    guess = int(input("Enter number here: "))
else: 
    print("well done, you took", count,  "attempts" )