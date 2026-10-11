from turtle import Turtle
LEN = 1
WID = 5
class Paddle(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=LEN, stretch_wid=WID)
        self.color(color)
        self.penup()
        self.goto(position)

    def up(self):
        self.goto(self.xcor(), self.ycor() + 10)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 10)
