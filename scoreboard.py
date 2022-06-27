from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update()

    def update(self):
        self.write("score " + str(self.score))

    def gameover(self):
        self.clear()
        self.write("Gameover. Your score is " + str(self.score))

    def increment(self):
        self.score +=1
        self.clear()
        self.update()