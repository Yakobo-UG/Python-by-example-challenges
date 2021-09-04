#Ask the user to enter the radius of a circle (measurement from the centre point to the edge). Work out the area of the circle (π*radius2).
import math
radius = float(input("Enter radius of circle: "))
x2 = radius*radius
pie = math.pi
answer = pie*x2
print(answer)
