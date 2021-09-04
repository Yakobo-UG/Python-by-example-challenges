#Display the following message: If the user enters 1 (square), then it should ask them for the length of one of its sides and display the area. If they select 2(triangel), it should ask for the base and height of the triangle and display the area. If they type in anything else, it should give them a suitable error message.

enter = float(input("Enter number here: "))
if enter == 1:
    length = float(input("Enter the lenght of one side: "))
    areasq = length*4
    print(areasq)
elif enter ==2:
    base = float(input("Enter the base: "))
    height = float(input("Enter height: "))
    areatr = 0.5*base*height
    print(areatr)
else: 
    print("Please use the allocated/given values")
    
    
    