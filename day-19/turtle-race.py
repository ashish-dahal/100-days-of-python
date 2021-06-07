from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = True
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color:"
)

colors = ["red", "orange", "yellow", "green", "blue"]
all_turtles = []
y_position = -70
for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(x=-230, y=y_position)
    y_position += 30
    all_turtles.append(turtle)


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
            is_race_on = False
        turtle.forward(random.randint(0, 10))
screen.exitonclick()
