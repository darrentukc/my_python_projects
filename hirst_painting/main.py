# import colorgram
# rgb_colors = []
# # Extract 6 colors from an image.
# colors = colorgram.extract('hirst.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

from turtle import Turtle, Screen
from random import randint

color_list = [(188, 165, 127), (127, 85, 66), (79, 97, 117), (145, 161, 174), (213, 202, 149), (159, 148, 65),
              (73, 40, 31), (78, 107, 87), (112, 42, 32), (146, 169, 149), (114, 87, 92), (180, 102, 88),
              (167, 150, 158), (45, 52, 62), (59, 42, 44), (218, 180, 172), (183, 93, 98), (109, 37, 40),
              (107, 140, 125), (103, 127, 157), (182, 202, 177), (215, 179, 184), (68, 70, 46), (46, 53, 49),
              (51, 62, 83), (184, 189, 205)]



ttt = Turtle()
ttt.shape('circle')
screen = Screen()
screen.colormode(255)


def random_color(list_of_colors):
    ran_color = list_of_colors[randint(0, len(list_of_colors) - 1)]
    r = ran_color[0]
    g = ran_color[1]
    b = ran_color[2]
    rgb_tuple = (r, g, b)
    return rgb_tuple


def draw_art(dimensionx, dimensiony):
    x_space = 600 / (dimensionx * 2)
    y_space = 500 / (dimensiony * 2)

    for factor in range(dimensiony):
        ttt.penup()
        new_y = -250 + ((y_space * 2) * factor)
        ttt.setx(-300)
        ttt.sety(new_y)

        for spot in range(dimensionx):
            if x_space < y_space:
                ttt.pensize(x_space)
            elif y_space < x_space:
                ttt.pensize(y_space)
            ttt.pencolor(random_color(color_list))
            ttt.pendown()
            ttt.fd(1)
            ttt.penup()
            ttt.fd(x_space * 2)

ttt.hideturtle()
ttt.speed('fastest')
draw_art(12,12)

screen = Screen()
screen.exitonclick()
