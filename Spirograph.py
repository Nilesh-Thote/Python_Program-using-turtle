import turtle as t
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(space):
    for i in range(int(360 / space)):
        picasso.color(random_color())
        picasso.circle(100)
        picasso.setheading(picasso.heading() + space)


picasso = t.Turtle()
t.colormode(255)
picasso.shape("turtle")
picasso.speed("fastest")
draw_spirograph(5)
s=t.Screen()
s.exitonclick()