#Ask the user to type in their postcode. Display the first two letters in uppercase. 
postcode = str(input("Enter your postcode: "))
upper = postcode[0:2].upper()
print(upper)