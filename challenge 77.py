#Change program 076 so that once the user has completed their list of names, display the full list and ask them to type in one of the names on the list. Display the position of that name in the list. Ask the user if they still want that person to come to the party. If they answer “no”, delete that entry from the list and display the list again. 
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

oneofname = str(input("Enter one of the names: "))
print(store.index(oneofname))
index = store.index(oneofname)

ask = str(input("Do you still want the pwrson to come to the party: "))
if ask == "n":
    del store[index]
    print(store)
else:
    if ask == "y":
        print(store)
        print("There are", len(store), "people ivited to the party")

    





    