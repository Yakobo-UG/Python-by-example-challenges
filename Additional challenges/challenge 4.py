#Please write a program which count and print the numbers of each character in a string input by console.
import collections
#counts horizontally and creates a list
UserInput = str(input("Enter words: "))
results = collections.Counter(UserInput)
print(results)
#counts vertically
UserInput = str(input("Enter words: "))
for i in UserInput:
    print(i ,",",UserInput.count(i))
    