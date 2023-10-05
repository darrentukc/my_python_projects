import colorgram
from turtle import Turtle, Screen
from random import randint

colors = colorgram.extract('matrix.jpg', 6)
color_list = []

for color in colors:
    r = color.rgb[0]
    g = color.rgb[1]
    b = color.rgb[2]
    rgb_tuple = (r, g, b)
    color_list.append(rgb_tuple)

def random_color(list_of_color):
    color = list_of_color[randint(0, len(list_of_color)-1)]
    r = color[0]
    g = color[1]
    b = color[2]
    rgb_tuple = (r, g, b)
    return rgb_tuple

tt = Turtle()
screen = Screen()
screen.colormode(255)
tt.right(90)
tt.speed('fastest')

line_length = 5

num_of_lines = int(500 / line_length)
num_of_lines_across = int(600/10)

for factor in range(num_of_lines_across):
    tt.penup()
    x = -300 + (factor * 10)
    tt.setx(x)
    tt.sety(250)
    for _ in range(num_of_lines):
        tt.width(10)
        tt.pencolor(random_color(color_list))
        tt.pendown()
        tt.fd(line_length)



screen.exitonclick()

