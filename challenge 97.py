#Using the 2D list from program 096, ask the user to select a row and a column and display that value. 
'''
    0   1   2
0   2   5   8
1   3   7   4
2   1   6   9
3   4   2   0

''' 
Simple2D = [ [2,5,8],[3,7,4], [1,6,9],[34,2,0] ]
askRow = int(input("Enter raw:"))
askColumn = int(input("Enter colomn: "))
print(Simple2D[askRow][askColumn])