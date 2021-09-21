#Display the following menu to the user: 
'''
1) Create new file
2) Display the file
3) Add a new file to the file, make a selction of 1,2 or 3:

Ask the user to enter 1, 2 or 3. If they select anything other than 1, 2 or 3 it should display a suitable error message.  
 If they select 1, ask the user to enter a school subject and save it to a new file called “Subject.txt”. It should overwrite any existing file with a new file.  
 If they select 2, display the contents of the “Subject.txt” file.  
 If they select 3, ask the user to enter a new subject and save it to the file and then display the entire contents of the file.  
Run the program several times to test the options. 
'''

print("1). Create new file: \n2). Display  file: \n3). Add new file to the file: ")
select = int(input("Enter number between 1,2,3: "))
if select == 1:
    ask1 = str(input("Enter a school subject: "))
    file1 = open("Subject.txt", "w")
    file1.write(ask1)
    file1.close()
elif select == 2:
    file1 = open("Subject.txt", "r")
    print(file1.read())
elif select == 3:
    ask2 = str(input("Enter new subject: "))
    file1 = open("Subject.txt", "a")
    file1.write(ask2)
    file1.close()
    #Displaying file
    file1 = open("Subject.txt", "r")
    print(file1.read())
else:
    print("Error not within the range")