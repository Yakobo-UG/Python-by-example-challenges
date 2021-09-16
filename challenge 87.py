#Ask the user to type in a word and then display it backwards on separate lines. For instance, if they type in “Hello” it should display as shown below
#o
#l
#l
#e
#H

word = str(input("Enter word: "))
length = len(word)
num = 1
for i in word:
    position = length - num
    letter = word[position]
    print(letter)
    num = num + 1
    