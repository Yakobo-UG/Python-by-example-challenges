#Write a function that validates whether two strings are identical. Make it case insensitive.
def valid(string1, string2):
    string1.lower()
    string2.lower()
    if string1 == string2:
        return "Is same"
    else:
        return "Not same"
print(valid("James", "James"))