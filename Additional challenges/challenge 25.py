'''
Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old. It will take your current age as the input and output a message with our time left in this format:
You have x days, y weeks, and z months left. Where x, y and z are replaced with the actual calculated numbers.
'''
import math
age = int(input("Enter your age: "))
sub = 90 - age
days = sub*365
weeks = sub*52
months = sub*12
print(f" you are left with {days} days {weeks} weeks {months} month to reach 90 years")

