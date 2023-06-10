from turtle import Turtle, xcor
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.goto(random.randint(-200, 200), 0)
        self.dir_x = 1
        self.dir_y = 1

    def move(self):
        newx = self.xcor() + 5 * self.dir_x
        newy = self.ycor() + 5 * self.dir_y
        self.goto(newx, newy)

    def bounce_x(self):
        self.dir_x *= -1

    def bounce_y(self):
        self.dir_y *= -1

    def reset_position(self):
        self.goto(0, -290)
        self.dir_x *= -1
        self.dir_y *= -1
