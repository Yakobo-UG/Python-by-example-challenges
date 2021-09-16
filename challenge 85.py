#Ask the user to type in their name and then tell them how many vowels are in their name.
name = str(input("Enter your name: "))
count = 0
for i in name:
    if  i == "a" or  i == "e" or  i == "i" or  i == "o" or  i == "u" :
        count = count + 1
print("There are ", count, "vowels in your name")