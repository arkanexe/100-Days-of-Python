import colorgram
import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
screen = t.Screen()

colors = colorgram.extract("image.jpg", 30)
color_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    if r and g and b > 210:
        continue
    color_list.append((r, g, b))


tim.setheading(225)
tim.penup()
tim.hideturtle()
tim.forward(300)
number_of_dots = 100
tim.setheading(0)
tim.speed("fastest")
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)


    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen.exitonclick()
