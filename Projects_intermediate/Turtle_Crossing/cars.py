from turtle import Turtle
from random import choice,randint

COLORS = ["blue", "green", "yellow", "red", "black"]
CARS_MOVEMENT = 10


class Cars(Turtle):

    def __init__(self,y):
        super().__init__()
        self.x_speed = CARS_MOVEMENT
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1,stretch_len=1.5)
        self.color(choice(COLORS))
        self.goto(randint(-300,600), y)

    def move_left(self):
        self.setx(self.xcor() - self.x_speed)

    def more_speed(self):
        self.x_speed += 10

    def reset_car(self):
        self.goto(randint(300,1000), randint(-240, 240))
