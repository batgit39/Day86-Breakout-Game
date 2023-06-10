import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from bricks import Bricks

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
screen.title("Breakout Game")
screen.bgcolor("black")

paddle = Paddle((0, -250))
ball = Ball()
bricks = Bricks()
bricks.make_bricks()

# Score
score = 0
score_pen = Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0, 260)
score_pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))

# Start message
start_message = Turtle()
start_message.speed(0)
start_message.color("white")
start_message.penup()
start_message.hideturtle()
start_message.goto(0, 0)
start_message.write("Press any key to start", align="center", font=("Courier", 24, "normal"))

screen.listen()

# Start game on key press
game_started = False
def start_game():
    global game_started
    if not game_started:
        game_started = True
        start_message.clear()

screen.onkey(start_game, "space")  # You can change "space" to any key you prefer

screen.onkey(paddle.right, "Right")
screen.onkey(paddle.left, "Left")

x = 0.01
while True:
    if game_started:
        time.sleep(x)
        screen.update()
        ball.move()

        collision_left_right_walls = (ball.xcor() > 380) or (ball.xcor() < -380)
        collision_top_wall = ball.ycor() > 290
        no_paddle_collision = ball.ycor() < -290

        if collision_left_right_walls:
            ball.bounce_x()

        if collision_top_wall:
            ball.bounce_y()

        # if no_paddle_collision:

        collision_paddle = (paddle.xcor() - 60 < ball.xcor() < paddle.xcor() + 60)
        ball_not_lost = ball.ycor() < -240

        if ball_not_lost and collision_paddle:
            ball.bounce_y()

        # Check for collision with the bricks
        for brick in bricks.bricks:
            collision_brick_xcor = (brick.xcor() - bricks.brick_width / 2 < ball.xcor() < brick.xcor() + bricks.brick_width / 2)
            collision_brick_ycor = (brick.ycor() - bricks.brick_height / 2 < ball.ycor() < brick.ycor() + bricks.brick_height / 2)
            collision_bricks = collision_brick_xcor and collision_brick_ycor
            if collision_bricks:
                brick.goto(1000, 1000)
                ball.bounce_y()
                score += 1
                score_pen.clear()
                score_pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

        game_over = ball.ycor() < -300 or score == 50
        if game_over:
            score_pen.goto(0, 0)
            score_pen.write("Game Over", align="center", font=("Courier", 24, "normal"))
            break

    else:
        screen.update()

screen.exitonclick()

