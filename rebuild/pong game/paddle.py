from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.color(color)
        self.penup()
        self.goto(position)

    def up(self):
        self.goto(self.xcor(), self.ycor() + 10)
        
    def down(self):
        self.goto(self.xcor(), self.ycor() - 10)
