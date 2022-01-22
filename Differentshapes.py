from turtle import Turtle, Screen
import random

Picasso = Turtle()
Picasso.shape("turtle")
color = ["red", "blue", "green", "orange", "yellow", "pink", "violet", "black", "brown"]
for sides in range(3, 11):
    angle = 360
    shape = angle / sides
    Picasso.color(random.choice(color))
    for j in range(sides):
        Picasso.rt(shape)
        Picasso.forward(100)

s = Screen()
s.exitonclick()