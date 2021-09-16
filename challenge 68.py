#Draw a pattern that will change each time the program is run. Use the random function to pick the number of lines, the length of each line and the angle of each turn.
import random
import turtle
numlines = random.randint(6,30)
length =  random.randint(20,50)
angle = random.randint(10,100)

for i in range(0,numlines ):
    turtle.forward(length)
    turtle.right(angle)
turtle.exitonclick()