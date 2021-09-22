#Using the Books.csv file, ask the user how many records they want to add to the list and then allow them to add that many. After all the data has been added, ask for an author and display all the books in the list by that author. If there are no books by that author in the list, display a suitable message.
import csv
file = open("Books.csv", "a")
ask = int(input("How many records do you want to enter: "))
for i in range(0,ask):
    Title = str(input("Enter book name: \n"))
    Auther = str(input("Enter Author: \n"))
    Year = str(input("Enter year: \n"))
    Newrecord = Title + "," + Auther + "," +  Year
    file.write(str(Newrecord))
file.close()
    
ask2 = input("What is the name of the Auther: ")
file = open("Books.csv", "r")
reader = csv.reader(file)
for i in file:
    if ask2 in str(i):
        print(i)
    else:
        print("Not aviable")
file.close()