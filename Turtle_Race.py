from turtle import Turtle, Screen
import random

color = ["red", "yellow", "green", "blue", "orange", "purple"]
turtle_obj = []
ycord = [-70, -40, -10, 20, 50, 80]
s = Screen()
s.setup(width=500, height=400)
for turtle in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.color(color[turtle])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=ycord[turtle])
    turtle_obj.append(new_turtle)
bet_color = s.textinput(title="Make a bet", prompt="which rainbow color turtle do you think will win?")
print(bet_color)

race = True
while race:
    for turtle in turtle_obj:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            race = False
            if winning_color == bet_color:
                print("You won")
            else:
                print(f"You lose, {winning_color} won")
        distance = random.randint(0, 10)
        turtle.fd(distance)

s.exitonclick()
