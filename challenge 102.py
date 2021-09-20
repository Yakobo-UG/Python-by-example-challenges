#Ask the user to enter the name, age and shoe size for four people. Ask for the name of one of the people in the list and display their age and shoe size. 
people = {"Tom": {"age": 23, "size":7 }, "Jimmy":{"age":45  , "size":87 }, "Billy": {"age": 56 , "size": 23}, "Zack": {"age": 79 , "size":5 }}
askPeople = input("Ask one person: ")
print(people[askPeople])