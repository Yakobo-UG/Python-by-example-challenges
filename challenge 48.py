#Ask for the name of somebody the user wants to invite to a party. After this, display the message “[name] has now been invited” and add 1 to the count. Then ask if they want to invite somebody else. Keep repeating this until they no longer want to invite anyone else to the party and then display how many people they have coming to the party.

repeat = "yes" 
repeat = "YES" 
repeat = "Yes" 
add = 0 
while repeat == "yes" or repeat == "Yes" or repeat == "YES" :
    name =str(input("Enter name to be invited: "))
    print (name, "has now been invited")
    add = add + 1
    repeat = str(input("Do you want to add another person?: "))
print(add, "number of peaple have been invited to the party")
