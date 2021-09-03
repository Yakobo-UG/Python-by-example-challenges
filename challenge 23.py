#Ask the user to type in the first line of a nursery rhyme and display the length of the string. Ask for a starting number and an ending number and then display just that section of the text (remember Python starts counting from 0 and not 1)

rhyme = str(input("Enter rhyme: "))
print(len(rhyme))
start_num = int(input("Enter start number: "))
end_num = int(input("Enter end number: "))
print(rhyme[start_num:end_num])
