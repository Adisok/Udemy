from turtle import Turtle, Screen
from random import randint, choice
import turtle


turtle.colormode(255)
albercik = Turtle()
albercik.speed(0)
albercik.penup()
albercik.setx(-250)
albercik.sety(-250)
albercik.hideturtle()


turtle_colors = [(201, 164, 112), (239, 246, 241), (152, 75, 50), (221, 201, 138), (57, 95, 126), (170, 152, 44),
                 (138, 31, 20), (135, 163, 183), (196, 94, 75), (49, 121, 88), (143, 177, 149), (95, 75, 77),
                 (76, 39, 32), (164, 146, 157), (16, 98, 71), (232, 176, 165), (54, 46, 48), (32, 61, 76), (22, 83, 89),
                 (182, 204, 176), (141, 22, 25), (86, 147, 127), (45, 66, 85), (8, 68, 53), (177, 94, 97),
                 (222, 177, 182), (109, 128, 151), (178, 191, 209), (85, 80, 34), (109, 136, 140), (255, 195, 0),
                 (173, 198, 202)]


for i in range(1, 101):
    y = albercik.ycor()

    albercik.dot(20, choice(turtle_colors))
    albercik.forward(50)
    if i % 10 == 0:
        albercik.setx(-250)
        albercik.sety(y + 50)

screen = Screen()
screen.exitonclick()
