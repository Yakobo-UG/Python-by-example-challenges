#Ask for the radius and the depth of a cylinder and work out the total volume (circle area*depth) rounded to three decimal places. 

import math


radius = float(input("Enter the radius: "))
depth = float(input("Enter depth: "))
area = math.pi*(radius**2)
print(round(area*depth))