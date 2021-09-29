#Create a function that takes two strings as arguments and return either True or False depending on whether the total number of characters in the first string is equal to the total number of characters in the second string.
def strings(a, b):
    if len(a) == len(b):
        return True
    else:
        return False
print(strings("James", "Muhumuza"))
