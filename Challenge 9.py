#Write a program that will ask for a number of days and then will show how many hours, minutes and seconds are in that number of days. 
Numdays = int(input("Enter the number: "))
NoHours = Numdays*24
NoMin = NoHours*60
NoSec = NoMin*60

print(" There are ", NoHours, "hours",  NoMin, "minutes and", NoSec, "seconds in", Numdays, "days")
