from turtle import Turtle, Screen
import colorgram
import random

colors = colorgram.extract("day-18/image.jpg", 30)
new_color = []
for i, color in enumerate(colors):
    new_color.append(tuple(colors[i].rgb))

print(random.choice(new_color))


turtle = Turtle()
screen = Screen()
screen.colormode(255)
screen.setworldcoordinates(0, 0, 500, 500)
turtle.penup()
turtle.speed("fastest")
for i in range(10):
    for j in range(10):
        turtle.dot(20, random.choice(new_color))
        turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.back(500)
screen.exitonclick()
