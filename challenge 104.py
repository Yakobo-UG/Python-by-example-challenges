#After gathering the four names, ages and shoe sizes, ask the user to enter the name of the person they want to remove from the list. Delete this row from the data and display the other rows on separate lines.
people = {"Tom": {"age": 23, "size":7 }, "Jimmy":{"age":45  , "size":87 }, "Billy": {"age": 56 , "size": 23}, "Zack": {"age": 79 , "size":5 }}
RemovePerson = input("Enter the name of person you want to be removed: ")
del people[RemovePerson]
for i in people:
    print(i)