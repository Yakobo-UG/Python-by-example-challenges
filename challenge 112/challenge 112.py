#Using the Books.csv file from program 111, ask the user to enter another record and add it to the end of the file. Display each row of the .csv file on a separate line.
import csv
from os import write
file = open("Books.csv", "a")
BookName = str(input("Enter Name of the book: "))
Auther = str(input("Enter name of the auther: "))
year = str(input("Enter year of the book:"))
NewRecode = BookName + ","  +  Auther + ", " +  year
file.write(str(NewRecode))
file.close()