#Ask the user to type in their favourite school subject. Display it with “-” after each letter, e.g. S-p-a-n-i-s-h-. 
bestsub = str(input("Enter your best school subject: "))
for i in bestsub:
    print(i, end="-")