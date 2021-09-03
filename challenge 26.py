#Pig Latin takes the first consonant of a word, moves it to the end of the word and adds on an “ay”. If a word begins with a vowel you just add “way” to the end. For example, pig becomes igpay, banana becomes ananabay, and aadvark becomes aadvarkway. Create a program that will ask the user to enter a word and change it into Pig Latin. Make sure the new word is displayed in lower case.

word = str(input("Enter word : "))
first = word[0]
#print(first)
lenght = len(word)
other = word[1: lenght]
#print(other)

if (first != "a" or first != "e" or  first != "o" or first != "u" or  first != "i" ):
    print(other + first + "ay")
else:
    print(word + "way")
