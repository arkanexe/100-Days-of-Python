# main.py
from turtle import Screen, Turtle
from clock import Clock

screen = Screen()
screen.setup(500, 500)
screen.tracer(0)

# TODO: draw the face (circle + 12 ticks) once, in a ClockFace class

turtle = Turtle()
turtle.circle(50)
clock = Clock(screen)
clock.update()

screen.mainloop()
