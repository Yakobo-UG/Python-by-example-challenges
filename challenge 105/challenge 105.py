#Write a new file called “Numbers.txt”. Add five numbers to the document which are stored on the same line and only separated by a comma. Once you have run the program, look in the location where your program is stored and you should see that the file has been created. The easiest way to view the contents of the new text fileon a Windows system is to read it using Notepad. 
NewFile = open("Numbers.txt","w")
NewFile.write("1,")
NewFile.write("2,")
NewFile.write("3,")
NewFile.write("4,")
NewFile.write("5,")
NewFile.close()