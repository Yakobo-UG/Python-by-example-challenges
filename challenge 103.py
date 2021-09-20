#Adapt program 102 to display the names and ages of all the people in the list but do not show their shoe size
people = {"Tom": {"age": 23, "size":7 }, "Jimmy":{"age":45  , "size":87 }, "Billy": {"age": 56 , "size": 23}, "Zack": {"age": 79 , "size":5 }}
for i in range(0,4):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    size =int(input("Enter size: "))
    people[name] = {"age": age, "size": size}
  
    
for name in people:
    print(name, people[name]["age"])
  