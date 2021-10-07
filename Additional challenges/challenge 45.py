'''
Make a function that encrypts a given input with these steps:
Input: "apple"
Step 1: Reverse the input: "elppa"
Step 2: Replace all vowels using the following chart:
a => 0
e => 1
o => 2
u => 3
Step 3: Add "aca" to the end of the word: "1lpp0aca"
Output: "1lpp0aca"
'''


def encrypt(word):
    backword = str(word[::-1])
    a = backword.replace("a", "0")
    b = a.replace("e", "1")
    c = b.replace("o", "2")
    d = c.replace("u", "3")
    e = d.replace("i", "4")
    return e + "aca"
print(encrypt(input("Enter word: ")))





