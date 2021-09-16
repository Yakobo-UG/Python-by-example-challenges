#Enter a list of ten colours. Ask the user for a starting number between 0 and 4 and an end number between 5 and 9. Display the list for those colours between the start and end numbers the user input.
colors = ["Red","Blue","Yellow","Pink","cyan","purple","violet","maroon","black","magenta"]
start = int(input("Enter number between 0 and 4"))
end = int(input("enter number betwwen 5 and 9"))
split = colors[start:end]
print(split)