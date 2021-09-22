#Please write a program which accepts a string from console and print the characters that have even indexes.
UserInput = str(input("Enter characters: "))
UserInput = UserInput[::2]
print(UserInput)