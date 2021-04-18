from turtle import Turtle

ALIGNMENT = "CENTER"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as f:
            self.high_score = int(f.read())
        self.speed("fastest")
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.ht()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increas_score(self):
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as f:
                f.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
