#Show the user a line of text from your favourite poem and ask for a starting and ending point. Display the characters between those two points. 
poem ="As man workth"
print(len(poem))
start = str(input("Enter start point: "))
startlen = len(start)
print(startlen)
end = str(input("Enter end point: "))
endlen = len(end)
print(endlen)
lengthpoem = len(poem)
print(poem[startlen:endlen])