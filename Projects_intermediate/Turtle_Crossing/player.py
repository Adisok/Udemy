from turtle import Turtle
STARTING_XY = (0, -280)
PLAYER_MOVEMENT = 20


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("chocolate")
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        self.forward(PLAYER_MOVEMENT)

    def go_to_start(self):
        self.goto(STARTING_XY)
