#Using the 2D list from program 096, ask the user which row they would like displayed and display just that row. Ask them to enter a new value and add it to the end of the row and display the row again.
'''
    0   1   2
0   2   5   8
1   3   7   4
2   1   6   9
3   4   2   0

'''
Simple2D = [ [2,5,8], [3,7,4], [1,6,9], [34,2,0] ]
askRow = int(input("Enter row: "))
print(Simple2D[askRow])

Newvalue = int(input("Enter new value: "))
Simple2D[askRow].append(Newvalue)
print(Simple2D[askRow])

