from turtle import Turtle, Screen

albercik = Turtle()
screen = Screen()


def move_forwards():
    albercik.forward(20)


def move_backwards():
    albercik.backward(20)


def counter_clockwise():
    albercik.left(10)


def clockwise():
    albercik.right(10)


def clear_drawning():
    albercik.clear()
    albercik.penup()
    albercik.setx(0)
    albercik.sety(0)
    albercik.pendown()


screen.listen()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_drawning)


screen.exitonclick()
