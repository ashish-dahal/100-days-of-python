from turtle import Turtle, goto

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="Left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align="Center", font=FONT)
