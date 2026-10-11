from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        # self.move()

    def move(self):
        x_axis = self.xcor() + self.x_move
        y_axis = self.ycor() + self.y_move

        self.goto(x_axis, y_axis)
    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1
