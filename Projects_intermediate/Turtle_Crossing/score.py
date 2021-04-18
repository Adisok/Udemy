from turtle import Turtle


class Levels(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.penup()
        self.ht()
        self.goto(-240, 260)
        self.show_level()

    def show_level(self):
        self.clear()
        self.write(f"Level : {self.level}", )

    def game_over(self):
        self.goto(-30, 0)
        self.write("Game Over")
