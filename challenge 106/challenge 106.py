#Create a new file called “Names.txt”. Add five names to the document, which are stored on separate lines. Once you have run the program, look in the location where your program is stored and check that the file has been created properly. 
NewFile = open("Names.txt", "w")
NewFile.write("John \n")
NewFile.write("Zick \n")
NewFile.write("luther \n")
NewFile.write("Mark \n")
NewFile.write("Jenin \n")
NewFile.close()