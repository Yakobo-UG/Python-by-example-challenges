#Draw an octagon that uses a different colour (randomly selected from a list of six possible colours) for each line
import turtle
import random

ran = random.choice(["Yellow", "Blue", "Black", "Pink", "Purple", "Cyan", "Maroon"])
turtle.pensize(5)
for i in range(0,8):

    turtle.color(ran)
    turtle.forward(100)
    turtle.right(45)


turtle.exitonclick()