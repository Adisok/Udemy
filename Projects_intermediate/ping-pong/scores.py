from turtle import Turtle


class Scores(Turtle):

    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.ht()
        self.goto(-0, 260)
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"{self.score1} : {self.score2}", align="center", font=("arial", 24, "normal"))

    def game_over(self):
        self.write("GAME OVER")
