from turtle import Turtle


class Gameboard():

    def __init__(self):
        self.middle = Turtle()
        self.middle.ht()
        self.middle.speed("fastest")
        self.middle.color("white")
        self.middle.penup()
        self.middle.goto(0, 300)
        self.middle.setheading(270)
        self.middle.width(5)
        self.draw_middle()

    def draw_middle(self):
        while self.middle.ycor() > -300:
            self.middle.pendown()
            self.middle.forward(30)
            self.middle.penup()
            self.middle.forward(30)
