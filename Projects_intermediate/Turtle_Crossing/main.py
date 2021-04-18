from turtle import Screen
from time import sleep
from player import Player
from cars import Cars
from random import randint
from score import Levels

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


player1 = Player()
cars = []
for _ in range(40):
    cars.append(Cars(randint(-240, 240)))

score_levels = Levels()

screen.onkey(player1.go_up, "Up")

game_on = True
while game_on:

    if player1.ycor() > 300:
        player1.go_to_start()
        score_levels.level += 1
        score_levels.show_level()
        for i in cars:
            i.more_speed()

    for i in cars:
        if player1.distance(i) < 20:
            score_levels.game_over()
            game_on = False
        if i.xcor() < -300:
            i.reset_car()
        i.move_left()
    sleep(0.1)
    screen.update()


screen.exitonclick()
