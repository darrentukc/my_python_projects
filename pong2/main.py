from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
from time import sleep

FIELD_WIDTH = 800
FIELD_HEIGHT = 600
ball_speed = 0.1
ANGLE = 45
game_is_on = True

screen = Screen()
screen.bgcolor('black')
screen.setup(width=FIELD_WIDTH, height=FIELD_HEIGHT)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball(ANGLE)
score = Score()


screen.listen()
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')
screen.onkey(r_paddle.go_up, key='Up')
screen.onkey(r_paddle.go_down, 'Down')

while game_is_on:

    ball.move(ball_speed)
    screen.update()

    # wall bounce
    if ball.ycor() > ((FIELD_HEIGHT / 2) - 10) or ball.ycor() < ((FIELD_HEIGHT / -2) + 20):
        ball.wall_bounce()

    # r paddle bounce
    elif 335 < ball.xcor() < 340:
        paddle_ycor = r_paddle.ycor()
        if (paddle_ycor - 50) < ball.ycor() < (paddle_ycor + 50):
            ball_speed += 0.01
            ball.paddle_bounce()

    # l paddle bounce
    elif -335 > ball.xcor() > -340:
        ball_speed += 0.01
        paddle_ycor = l_paddle.ycor()
        if (paddle_ycor - 50) < ball.ycor() < (paddle_ycor + 50):
            ball_speed += 0.01
            ball.paddle_bounce()

    # if l player scores
    elif ball.xcor() > 400:
        score.l_point()
        ball.restart()
        ball_speed = 0.1
        ball.paddle_bounce()

    # if player 2 scores
    elif ball.xcor() < -400:
        score.r_point()
        ball.restart()
        ball_speed = 0.1
        ball.paddle_bounce()








screen.exitonclick()
