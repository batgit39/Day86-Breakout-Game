import turtle

# Set up the screen
window = turtle.Screen()
window.title("Breakout Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

# Bricks
bricks = []
brick_colors = ["red", "orange", "yellow", "green", "blue"]
brick_width = 80
brick_height = 20
brick_rows = 5
brick_columns = 10

for row in range(brick_rows):
    for column in range(brick_columns):
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(brick_colors[row // 2])
        brick.shapesize(stretch_wid=1, stretch_len=2)
        brick.penup()
        x = -350 + column * brick_width
        y = 250 - row * brick_height
        brick.goto(x, y)
        bricks.append(brick)

# Score
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0, 260)
score_pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))


# Functions to move the paddle
def paddle_left():
    x = paddle.xcor()
    if x > -350:
        x -= 20
    paddle.setx(x)


def paddle_right():
    x = paddle.xcor()
    if x < 350:
        x += 20
    paddle.setx(x)


# Keyboard bindings
window.listen()
window.onkeypress(paddle_left, "Left")
window.onkeypress(paddle_right, "Right")

# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check for collision with the walls
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
    elif ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    elif ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1

    # Check for collision with the paddle
    if (ball.ycor() < -240) and (ball.ycor() > -250) and (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        print("collision")
        ball.sety(-240)
        ball.dy *= -1

    # Check for collision with the bricks
    for brick in bricks:
        if (brick.ycor() - brick_height / 2 < ball.ycor() < brick.ycor() + brick_height / 2) and \
                (brick.xcor() - brick_width / 2 < ball.xcor() < brick.xcor() + brick_width / 2):
            brick.goto(1000, 1000)  # Move the brick off-screen
            ball.dy *= -1
            score += 1
            score_pen.clear()
            score_pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    # Check for game over
    if ball.ycor() < -300:
        score_pen.goto(0, 0)
        score_pen.write("Game Over", align="center", font=("Courier", 24, "normal"))
        break
