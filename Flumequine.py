import turtle as t
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_circle(ycordinates):
    for i in range(0, 500, 50):
        picasso.color(random_color())
        picasso.penup()
        picasso.setposition(-250 + i, ycordinates)
        picasso.pendown()
        picasso.begin_fill()
        picasso.circle(20)
        picasso.end_fill()


picasso = t.Turtle()
t.colormode(255)
picasso.shape("turtle")
picasso.speed("fastest")
ycord = -250
for i in range(0, 500, 50):
    draw_circle(ycord)
    ycord += 50

s = t.Screen()
s.exitonclick()
