#Please write a program which accepts a string from console and print it in reverse order.
UserInput = str(input("Enter words: "))
UserInput = UserInput[:: -1]
print(UserInput)