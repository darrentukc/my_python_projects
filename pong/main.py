from turtle import Turtle, Screen
from field import PlayField
from playerpaddle import PlayerPaddle
from computerpaddle import ComputerPaddle
from ball import Ball
from time import sleep

FIELD_WIDTH = 800
FIELD_HEIGHT = 600
PADDLE_SIZE = 5
COMPUTER_SPEED = 0.02
game_is_on = True
screen = Screen()

# TODO: create the screen
playingfield = PlayField(FIELD_WIDTH, FIELD_HEIGHT)

# TODO: create player paddle

player_paddle = PlayerPaddle(FIELD_WIDTH, FIELD_HEIGHT)
player_paddle.create(PADDLE_SIZE)

# TODO: create computer paddle

computer_paddle = ComputerPaddle(FIELD_WIDTH, FIELD_HEIGHT)
computer_paddle.create(PADDLE_SIZE)

# TODO: create ball

ball = Ball(FIELD_WIDTH, FIELD_HEIGHT)

screen.tracer(0)
screen.listen()
screen.onkeypress(player_paddle.up, key='w')
screen.onkeypress(player_paddle.down, key='s')

while game_is_on:
    computer_paddle.move(COMPUTER_SPEED)
    ball.move()
    screen.update()

    # top wall collision check

# TODO: create the ball and make it move
# TODO: detect colision with wall and bounce
# TODO: detect collision with paddle
# TODO: detect when paddle misses
# TODO: keep score


screen.exitonclick()
