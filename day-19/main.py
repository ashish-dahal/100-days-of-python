from turtle import Turtle, Screen
import turtle

screen = Screen()
tim = None


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_counter():
    tim.left(10)


def move_clock():
    tim.right(10)


def clear_canvas():
    screen.reset()


tim = Turtle()

screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=move_counter)
screen.onkeypress(key="d", fun=move_clock)
screen.onkeypress(key="c", fun=clear_canvas)

screen.exitonclick()
