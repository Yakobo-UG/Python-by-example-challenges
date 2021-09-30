'''
Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

Based on a user's order, work out their final bill.

Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25
Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: + $1
'''
bill = 0
Pizza = str(input("Ente rthe size of the pizza: "))
if Pizza == "small":
    bill = bill + 15
    print(bill)
elif Pizza == "Medium":
    bill = bill + 20
    print(bill)
elif Pizza == " Large":
    bill = bill + 25
    print(bill)
Pepperoni = str(input("Enter the size of the pepperoni: "))
if Pepperoni == "small":
    bill = bill + 2
    print(bill)
elif Pepperoni == "medium" or "large":
    bill = bill + 3
    print(bill)