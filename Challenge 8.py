#Ask for the total price of the bill, then ask how many diners there are. Divide the total bill by the number of diners and show how much each person must pay

dinnerprice = int(input("how much is the bill: "))
Noofdinners = int(input("how many dinners have u had: "))
paypereach = dinnerprice/Noofdinners
print("Each person will be paying: ", paypereach)