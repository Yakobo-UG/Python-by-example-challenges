#Change your previous program to ask the user which row they want displayed. Display that row. Ask which column in that row they want displayed and display the value that is held there. Ask the user if they want to change the value. If they do, ask for a new value and change the data. Finally, display the whole row again. 
'''
    0   1   2
0   2   5   8
1   3   7   4
2   1   6   9
3   4   2   0

'''
Simple2D = [ [2,5,8], [3,7,4], [1,6,9], [34,2,0] ]
askRow = int(input("Which row do you want to display: "))
print(Simple2D[askRow])
askColumn = int(input("Which colomn: "))
print(Simple2D[askRow][askColumn])

Change = str(input("Do you want to change the value: "))
if Change == "yes":
    NewValue = int(input("Enter new value: "))
    Simple2D[askRow][askColumn] = NewValue

print(Simple2D[askRow])