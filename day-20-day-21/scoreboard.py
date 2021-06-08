from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier new", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.SCORE = -1
        self.penup()
        self.fillcolor("white")
        self.color("white")
        self.hideturtle()
        self.goto(0, 300)
        self.update_score()

    def update_score(self):
        self.SCORE += 1
        self.clear()
        self.write(f"Score: {self.SCORE}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER. Press SPACE to play again!", align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        self.reset()
        self.__init__()
