#Ask the user to enter their favourite colour. If they enter “red”, “RED” or “Red” display the message “I like red too”, otherwise display the message “I don’t like [colour], I prefer red”. 

Color = str(input("Enter your favourite color: "))
if Color == "red" or Color == "RED" or Color == "Red": 
    print("i like red too")
else:
    print(" don't like ", Color, "i prefer red")