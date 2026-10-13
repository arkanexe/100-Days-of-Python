from turtle import Turtle
FONT = ("Courier", 22, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.display_score()


    def display_score(self):
        self.score += 1
        self.goto(-30, 250)
        self.clear()
        self.write(f"Level: {self.score}", align="RIGHT", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="CENTER", font=FONT)
    