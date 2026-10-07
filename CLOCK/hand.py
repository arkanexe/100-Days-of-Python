# hand.py
from turtle import Turtle

class Hand(Turtle):
    def __init__(self, length, thickness, color):
        super().__init__()
        self.length = length
        self.hideturtle()
        self.color(color)
        self.pensize(thickness)

    def point_to(self, clock_angle):
        self.clear()
        self.penup()
        self.goto(0, 0)
        self.setheading(90 - clock_angle)
        self.pendown()
        self.forward(self.length)
