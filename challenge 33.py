#Ask the user to enter two numbers. Use whole number division to divide the first number by the second and also work out the remainder and display the answer in a user-friendly way (e.g. if they enter 7 and 2 display “7 divided by 2 is 3 with 1 remaining”).

first = float(input("Enter first numbers: "))
second = float(input("Enter second numbers: "))
whole = first//second
remainder = first%second
print("if ", first, "is divided by ", second, "the answer is ", whole, "and a remainder of ", remainder )