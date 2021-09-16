#Ask the user to type in a word in upper case. If they type it in lower case, ask them to try again. Keep repeating this until they type in a message all in uppercase.
word = str(input("Enter a word in uppercase: "))
while word != word.upper():
    print("Try again")
    word = str(input("Enter a word in uppercase: "))
else:
    print("It is now upper:", word)
    



