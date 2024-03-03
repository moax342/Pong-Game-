from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreBoard import ScoreBoard

# all data associated with the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("Black")
screen.listen()
screen.tracer(100)

# creating the left and the right paddle
r_paddle = Paddle((380, 0))
l_paddle = Paddle((-390, 0))

# creating the ball
ball = Ball()
# creating the left and the right Score and giving them a position
r_scoreboard = ScoreBoard((30, 260))
l_scoreboard = ScoreBoard((-30, 260))

# control the paddle movement
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_moving()

    # Detecting collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detecting collision with the right paddle
    if ball.distance(r_paddle) < 30 and ball.xcor() > 320 \
            or ball.distance(l_paddle) < 30 and ball.xcor() < -320:
        ball.bounce_x()
        ball.move_speed *=0.9

    # Detecting collision with the wall
    if ball.xcor() > 380:
        l_scoreboard.add_point()
        ball.reset_position()
    elif ball.xcor() < -380:
        r_scoreboard.add_point()
        ball.reset_position()


screen.exitonclick()
