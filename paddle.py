from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid = 1, stretch_len = 5)
        self.goto(position)

    def left(self):
        if self.xcor() > -350:
            x = self.xcor() - 20
            self.goto(x, self.ycor())

    def right(self):
        if self.xcor() < 330:
            x = self.xcor() + 20
            self.goto(x, self.ycor())
