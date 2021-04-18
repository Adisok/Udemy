from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Pick Your color", prompt="Wich turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


def turtle_machine(col):
    tortiose = Turtle(shape="turtle")
    tortiose.color(colors[col])
    tortiose.penup()
    tortiose.goto(x=-230, y=-100 + i*40)
    return tortiose


turtles = []
for i in range(len(colors)):
    turtles.append(turtle_machine(i))

race = False

if user_bet:
    race = True

while race:
    for runner in turtles:
        runner.forward(randint(0, 10))
        if runner.xcor() >= 230:
            race = False
            winning_color = runner.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")

            else:
                print(f"You've lost! The {winning_color} turtle is the winner")


screen.exitonclick()
