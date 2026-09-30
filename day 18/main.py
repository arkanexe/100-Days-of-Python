# from turtle import Turtle, Screen

# tim = Turtle()






import turtle as t
import random

tim = t.Turtle()

# for i in range(3, 11):
#     tim.color(random.choice(colors))
#     for j in range(i):
#         tim.forward(100)
#         tim.right(360 / i)

t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)
# directions = [0, 90, 180, 270]
# tim.pensize(15)
tim.speed("fastest")

# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))




def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        # tim.setheading(tim.heading() + size_of_gap)
        tim.left(size_of_gap)

draw_spirograph(10)

screen = t.Screen()
screen.exitonclick()
