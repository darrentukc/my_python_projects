import turtle
from turtle import Turtle, Screen
from random import randint
from time import sleep


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
segments = []

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)


def move():
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(x=new_x, y=new_y)

    segments[0].forward(MOVE_DISTANCE)

def turn_right():
    if segments[0].heading() != 180:
        segments[0].setheading(0)

def turn_up():
    if segments[0].heading() != 270:
        segments[0].setheading(90)

def turn_left():
    if segments[0].heading() != 0:
        segments[0].setheading(180)

def turn_down():
    if segments[0].heading() != 90:
        segments[0].setheading(270)

for position in STARTING_POSITIONS:
    new_seg = Turtle(shape='square')
    new_seg.speed('normal')
    new_seg.color('white')
    new_seg.penup()
    new_seg.goto(position)
    segments.append(new_seg)


# screen.listen()
# screen.onkey(fun=snake.up , key='Up')
# screen.onkey(fun=snake.down , key='Down')
# screen.onkey(fun=snake.left , key='Left')


game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    screen.listen()
    screen.onkey(fun=turn_right, key='Right')
    screen.onkey(fun=turn_up , key='Up')
    screen.onkey(fun=turn_down , key='Down')
    screen.onkey(fun=turn_left , key='Left')
    move()


screen.exitonclick()