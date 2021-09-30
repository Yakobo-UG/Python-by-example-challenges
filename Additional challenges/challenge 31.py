'''You are going to write a program that tests the compatibility between two people. We're going to use the super scientific method recommended by BuzzFeed.To work out the love score between two people:
Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.
'''
Person1 = str(input("Enter your name: "))
Person2 = str(input("Enter your name: "))
together = (Person1 + Person2).lower()

t = together.count("t")
r = together.count("r")
u = together.count("u")
e = together.count("e")

l = together.count("l")
o = together.count("o")
v = together.count("v")
e = together.count("e")

true = t+r+u+e
love = l+o+v+e

true_love = int(str(true)+str(love))

if true_love < 10 or true_love > 90:
    print(f"Your score is {true_love}")
elif 40 <= true_love <= 50:
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}")
