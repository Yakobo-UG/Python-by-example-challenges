#Write the numbers as shown below "1,2,3", starting at the bottom of the number one.
import turtle
import random
ran = random.choice(["Yellow", "Blue", "Black", "Pink", "Purple", "Cyan", "Maroon"])
ran1 = random.choice(["Yellow", "Blue", "Black", "Pink", "Purple", "Cyan", "Maroon"])
ran2 = random.choice(["Yellow", "Blue", "Black", "Pink", "Purple", "Cyan", "Maroon"])

turtle.color(ran)
turtle.left(90)
turtle.forward(100)
turtle.penup()

turtle.right(90)
turtle.forward(100)

turtle.pendown()
turtle.forward(100)
turtle.right(90)
turtle.color(ran1)
turtle.penup

turtle.pendown()
turtle.left(1)
turtle.forward(90)

turtle.forward(100)
turtle.right(1)


turtle.exitonclick()

#got to lazy to finish this challenge but understood it, thats what matters hahaha