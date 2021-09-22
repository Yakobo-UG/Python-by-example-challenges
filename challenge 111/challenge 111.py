'''
Create a .csv file that will store the following data. Call it “Books.csv”. 
 
       Book                                     Author                          Year Released 
0     To Kill A Mockingbird                     Harper Lee                       1960 
1     A Brief History of Time Stephen           Hawking                          1988 
2     The Great Gatsby                          F. Scott Fitzgerald              1922 
3     The Man Who Mistook His Wife for a Hat    Oliver Sacks                     1985 
4      Pride and Prejudice                      Jane Austen                     1813 

'''
import csv
file = open("Books.csv", "w")
Title = "Book                                     Author                          Year Released \n"
One = "A Brief History of Time Stephen           Hawking                          1988 \n"
Two = " To Kill A Mockingbird                     Harper Lee                       1960 \n"
three = " The Great Gatsby                          F. Scott Fitzgerald              1922 \n"
Four = " The Man Who Mistook His Wife for a Hat    Oliver Sacks                     1985\n"
Five = "Pride and Prejudice                      Jane Austen                     1813 \n"

file.write(str(Title))
file.write(str(One))
file.write(str(Two))
file.write(str(three))
file.write(str(Four))
file.write(str(Five))
file.close()
