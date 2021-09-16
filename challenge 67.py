#dDraw a spiral octagon

import turtle

turtle.pensize(5)
for i in range(0,10):
    for i in range(0,8):
        turtle.forward(100)
        turtle.right(45)
    turtle.right(40)


turtle.exitonclick()