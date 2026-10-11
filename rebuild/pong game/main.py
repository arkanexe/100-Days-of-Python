from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

r_paddle = Paddle((265, 40), "green")
l_paddle = Paddle((-265, -40), "orange")

ball = Ball()
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
game_is_on = True

while game_is_on:
    screen.update()
screen.exitonclick()
