#Ask for a number below 50 and then count down from 50 to that number, making sure you show the number they entered in the output

Num = int(input("ENter number below 50: "))
if Num >= 50:
    print("Use a number belew 50")
else: 
    for i in range(50, Num, -1):
        print(i)

   