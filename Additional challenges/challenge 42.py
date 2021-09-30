#Create a function that takes a number (from 1 - 60) and returns a corresponding string of hyphens.
num = int(input("Enter number between 1 - 60: " ))
def num_to_dashes(num):
    if num in range(1,60):
        return (num * "-")
    else:
        return "Enter between 1 - 60"
print(num_to_dashes(num))