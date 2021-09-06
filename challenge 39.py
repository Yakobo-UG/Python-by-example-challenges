#Ask the user to enter a number between 1 and 12 and then display the times table for that number.

Num = int(input("Enter number between 1 and 12: "))
for i in range(1,13):
    print( Num, "x",i ,"=", Num*i)
