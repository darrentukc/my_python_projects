import turtle
from turtle import Turtle, Screen
from random import randint

# initializing

screen = Screen()
ttt = Turtle()
ttt.shape('turtle')
ttt.color('DeepSkyBlue2')
turtle.colormode(255)


def draw_square():
    for _ in range(0, 4):
        ttt.forward(100)
        ttt.right(90)


def draw_dash_line(dist):
    for _ in range(dist):
        ttt.fd(10)
        ttt.penup()
        ttt.fd(10)
        ttt.pendown()


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rgb_tuple = (r, g, b)
    return rgb_tuple


def draw_flower(num):
    if num < 3:
        print('Number has to be 3 or more')
    else:
        for num_of_angles in range(3, num + 1):
            inner_angle = 360 / num_of_angles
            ttt.color(random_color())
            for _ in range(0, num_of_angles):
                ttt.forward(100)
                ttt.right(inner_angle)


def random_walk(steps):
    ttt.pensize(10)
    direction = [90, 270, 0, 180]
    ttt.speed(10)
    for _ in range(0, steps):
        screen.colormode(255)
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        ttt.color(r, g, b)
        new_direction = direction[randint(0, 3)]
        ttt.seth(new_direction)
        ttt.fd(25)


def draw_circles(num_of_circles):
    gap_size = 360 / num_of_circles
    ttt.speed('fastest')
    heading = 0
    while heading <= 360:
        ttt.color(random_color())
        ttt.circle(100)
        heading += gap_size
        ttt.seth(heading)


draw_circles(200)

screen.exitonclick()
