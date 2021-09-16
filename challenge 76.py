#Ask the user to enter the names of three people they want to invite to a party and store them in a list. After they have entered all three names, ask them if they want to add another. If they do, allow them to add more names until they answer “no”. When they answer “no”, display how many people they have invited to the party.

store = []
person1 = str(input("Enter names first person: "))
person2 = str(input("Enter names second person: "))
person3 = str(input("Enter names third person: "))
store.append(person1) 
store.append(person2) 
store.append(person3) 
add = str(input("Do you want to add another: "))
while add == "y":
    person = str(input("Enter another person: "))
    store.append(person)
    add = str(input("Do you want to add another: "))
else:
    print("There are", len(store), "peaple invited to the party")
    print(store)
    