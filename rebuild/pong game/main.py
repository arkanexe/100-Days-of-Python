from turtle import Screen
from paddle import Paddle
from ball import Ball
from divider import Divider
import time
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0), "green")
l_paddle = Paddle((-350, 0), "orange")

ball = Ball()
divider = Divider()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()




screen.exitonclick()
