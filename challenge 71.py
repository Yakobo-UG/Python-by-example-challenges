#Create a list of two sports. Ask the user what their favourite sport is and add this to the end of the list. Sort the list and display it. 
sports = ["Football", "Basketball"]
user = str(input("Enter your best sport: "))
sports.append(user)
sports.sort()
print(sports)