from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snakerinio")
screen.tracer(0)
alberciki = []

blocks = 3

snakes = Snake()
food = Food()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(snakes.up, "Up")
screen.onkey(snakes.down, "Down")
screen.onkey(snakes.left, "Left")
screen.onkey(snakes.right, "Right")

game = True
while game:
    screen.update()
    time.sleep(0.1)
    snakes.snake_move()

    # Collision with food
    if snakes.head.distance(food) < 15:
        scoreboard.increas_score()
        snakes.extend_snake()
        food.refresh()

    # wall colision
    if snakes.head.xcor() > 290 or snakes.head.ycor() > 290 or snakes.head.xcor() < -290 or snakes.head.ycor() < -290:
        scoreboard.reset()
        snakes.reset()
    # ail colision
    for tail in snakes.alberciki[:-1]:
        if snakes.head.distance(tail) < 5:
            scoreboard.reset()
            snakes.reset()

screen.exitonclick()
