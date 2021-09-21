#Using the Names.txt file you created earlier, display the list of names in Python. Ask the user to type in one of the names and then save all the names except the one they entered into a new file called Names2.txt. 

#creating the file
NewFile = open("Name.txt", "w")
NewFile.write("jamse \n")
NewFile.write("Timmy \n")
NewFile.write("zick \n")
NewFile.close

#reading the file in terrminal
NewFile = open("Name.txt", "r")
print(NewFile.read())
NewFile.close()

#typing one of the names
NewFile = open("Name.txt", "r")
OneOftheNames = str(input("Type in one of the names: "))
for i in NewFile:
    if i != OneOftheNames:
        NewFile = open("Name2.txt", "a")
        NewFile.write(i)
        NewFile.close()
NewFile.close()
#reading the file
NewFile = open("Name2.txt", "r")
print(NewFile.read())

#failed to do it

