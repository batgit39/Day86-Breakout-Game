from turtle import Turtle


class Bricks(Turtle):

    def __init__(self):
        super().__init__()
        self.bricks = []

        self.brick_colors = ["red", "blue", "green", "pink", "yellow"]

        self.brick_width = 80
        self.brick_height = 20
        self.brick_rows = 5
        self.brick_columns = 10

    def make_bricks(self):
        for row in range(self.brick_rows):
            for column in range(self.brick_columns):
                brick = Turtle("square")
                brick.color(self.brick_colors[row])
                brick.shapesize(stretch_wid=1, stretch_len=2)
                brick.penup()
                x = -350 + column * self.brick_width
                y = 250 - row * self.brick_height
                brick.goto(x, y)
                self.bricks.append(brick)


# screen = Screen()
# screen.setup(width=800, height=600)
# screen.title("Breakout Game")
# screen.bgcolor("black")

# bricks = Bricks()
# bricks.make_bricks()

# screen.mainloop()
