#Open the Names.txt file. Ask the user to input a new name. Add this to the end of the file and display the entire file. 
#creating the file
NewFile = open("Name.txt", "w")
NewFile.write("jamse \n")
NewFile.write("Timmy \n")
NewFile.write("zick \n")
NewFile.close


#appending to file
ask = str(input("Enter new name: "))
NewFile = open("Name.txt", "a")
NewFile.write(ask)
NewFile.close()

#reading the file in terrminal
NewFile = open("Name.txt", "r")
print(NewFile.read())