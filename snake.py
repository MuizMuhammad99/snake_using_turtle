from turtle import Turtle

starting_snake_position = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segment = []
        self.create()

    def create(self):
        for position in starting_snake_position:
            self.add(position)

    def add(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segment.append(new_segment)

    def extend(self):
        self.add(self.segment[-1].position())

    def move(self):
        for segments in range(len(self.segment) - 1, 0, -1):
            x = self.segment[segments - 1].xcor()
            y = self.segment[segments - 1].ycor()
            self.segment[segments].goto(x, y)
        self.segment[0].forward(20)

    def up(self):
        if (self.segment[0].heading() != 270):
            self.segment[0].setheading(90)

    def down(self):
        if (self.segment[0].heading() != 90):
            self.segment[0].setheading(270)

    def left(self):
        if (self.segment[0].heading() != 0):
            self.segment[0].setheading(180)

    def right(self):
        if (self.segment[0].heading() != 180):
            self.segment[0].setheading(0)