from turtle import Turtle
import random


def random_walk(ang):
    picasso.color(random.choice(color))
    picasso.rt(ang)
    picasso.forward(30)


picasso = Turtle()
picasso.shape("turtle")
color = ["red", "blue", "green", "orange", "yellow", "pink", "violet",
         "CornFlowerBlue", "brown", "DarkOrchid", "LightSeaGreen", "SlateGray", "SeaGreen"]
direction = [0, 90, 180, 270]
picasso.width(15)
picasso.speed(10)
for i in range(200):
    random_walk(random.choice(direction))
