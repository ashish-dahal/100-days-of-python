from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Screen, Turtle
import time

WALL_BOUNDRY = 320
BORDER = WALL_BOUNDRY - 30
ALIGNMENT = "center"
FONT = ("Courier new", 14, "normal")
game_is_on = False
snake = food = scoreboard = border = prompt = screen = None


def initialize_board():
    global snake, food, scoreboard, border, prompt
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    border = Turtle()
    border.penup()
    border.pencolor("green")
    border.setposition(-BORDER, -BORDER)
    border.pendown()
    border.pensize(3)
    for i in range(4):
        border.forward(BORDER * 2)
        border.left(90)
    border.hideturtle()

    prompt = Turtle()
    prompt.penup()
    prompt.goto(0, 20)
    prompt.color("white")
    prompt.write(
        "Press SPACE to start the game!",
        align=ALIGNMENT,
        font=FONT,
    )
    prompt.hideturtle()

    screen.update()
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.up, "w")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.right, "d")
    screen.onkey(start_game, "space")
    screen.exitonclick()


def start_game():
    global game_is_on, snake, food, scoreboard, border, prompt
    prompt.reset()
    scoreboard.reset_scoreboard()
    food.refresh()
    snake.reset_snake()
    screen.onkey(None, "space")
    game_is_on = True

    while game_is_on:
        screen.update()
        time.sleep(0.1)

        snake.move()

        # Detect Collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            scoreboard.update_score()
            snake.extend()

        # Detect collision with wall
        if BORDER < abs(snake.head.xcor()) or BORDER < abs(snake.head.ycor()):
            scoreboard.game_over()
            screen.onkey(start_game, "space")
            game_is_on = False

        # Detect collision with wall
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.game_over()
                screen.onkey(start_game, "space")
                game_is_on = False


if __name__ == "__main__":

    screen = Screen()
    screen.setup(width=WALL_BOUNDRY * 2, height=WALL_BOUNDRY * 2)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    initialize_board()
