from turtle import Turtle


START_POSITION = [(-20, 0), (0, 0), (20, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.alberciki = []
        self.creat_snake()
        self.head = self.alberciki[-1]
        self.head.setheading(180)
        self.head.color("green")

    def creat_snake(self):
        for i in START_POSITION:
            self.add_segment(i)

    def snake_move(self):
        for albercik_num in range(0, len(self.alberciki) - 1, 1):
            x = self.alberciki[albercik_num + 1].xcor()
            y = self.alberciki[albercik_num + 1].ycor()
            self.alberciki[albercik_num].goto(x, y)
        self.alberciki[-1].forward(MOVE_DISTANCE)

    def add_segment(self, pos):
        new_turtle = Turtle(shape="square")
        new_turtle.penup()
        new_turtle.color("white")
        new_turtle.goto(pos)
        self.alberciki.insert(0, new_turtle)

    def extend_snake(self):
        self.add_segment(self.alberciki[0].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for albercik in self.alberciki:
            albercik.goto(1000, 1000)
        self.alberciki.clear()
        self.creat_snake()
        self.head = self.alberciki[-1]
        self.head.setheading(180)
        self.head.color("green")
