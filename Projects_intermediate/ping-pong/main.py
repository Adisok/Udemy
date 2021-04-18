from turtle import Screen
from players import Players
from board import Gameboard
from scores import Scores
from ball import Ball
from time import sleep

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Invalid-Pong")
screen.tracer(0)

score = Scores()
gameborad = Gameboard()
player1 = Players(-350, 0)
player2 = Players(350, 0)
ball = Ball()

screen.update()
screen.listen()

screen.onkeypress(player1.up, "Up")
screen.onkeypress(player1.down, "Down")

screen.onkeypress(player2.up, "w")
screen.onkeypress(player2.down, "s")
ball.move()

on = True

while on:
    ball.move()

    sleep(ball.move_speed)
    screen.update()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # detect collision with players
    if ball.xcor() > 320 and ball.distance(player2) < 50 or ball.xcor() < -320 and ball.distance(player1) < 50:
        ball.bounce_player()
        # ball.maximum_power()

    # Detect when paddle misses

    if ball.xcor() > 380:
        score.score1 += 1
        score.print_score()
        ball.reset_pos()

    if ball.xcor() < -380:
        score.score2 += 1
        score.print_score()
        ball.reset_pos()

screen.exitonclick()
