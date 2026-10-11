
from turtle import Turtle

LINE_NUMBER = 25


class Divider:
    def __init__(self):
        self.segments = []
        self.add_line()

    def create_shape(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        new_segment.shapesize(stretch_wid=1, stretch_len=0.05)
        self.segments.append(new_segment)

    def add_line(self):
        for index in range(LINE_NUMBER):
            pos = (0, 300 - index * 30)
            self.create_shape(pos)
