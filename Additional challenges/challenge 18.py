#Create a function that takes a single string as argument and returns an ordered list containing the indexes of all capital letters in the string.

def string(word):
    return [index for index, letter in enumerate(word) if letter.isupper()]
print(string("JaMes"))


