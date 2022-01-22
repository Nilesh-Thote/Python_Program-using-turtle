"""Press 'w' to move forward
    's' to move backward
    'a' to rotate anticlockwise
    'd' to rotate clockwise
    'c' to clear canvas
    """
from turtle import Turtle, Screen


def forward():
    picasso.forward(10)


def backward():
    picasso.backward(10)


def anticlockwise():
    picasso.left(10)


def clockwise():
    picasso.right(10)


def clear():
    picasso.home()
    picasso.clear()


picasso = Turtle()
s = Screen()
s.listen()
s.onkey(key="w", fun=forward)
s.onkey(key="s", fun=backward)
s.onkey(key="a", fun=anticlockwise)
s.onkey(key="d", fun=clockwise)
s.onkey(key="c", fun=clear)
s.exitonclick()
