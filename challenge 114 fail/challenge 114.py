#Using the Books.csv file, ask the user to enter a starting year and an end year. Display all books released between those two years. 
import csv
start = str(input("ENter a start year: "))
end = str(input("Enter an end year: "))
file = open("Books.csv", "r")
reader = csv.reader(file)
tmp = []
for i in file:
    tmp.append(i)
x = 0
for i in range(int(start) , int(end)):
    print(i)
#failed
