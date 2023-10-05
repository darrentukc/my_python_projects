from turtle import Turtle, Screen
from random import random, randint

screen = Screen()
screen.setup(width=500, height=500)
race_is_on = False
play_again = True


def rand_rgb():
    screen.colormode(255)
    r = randint(1, 255)
    g = randint(1, 255)
    b = randint(1, 255)
    rgb_tuple = (r, g, b)
    return rgb_tuple


while play_again:

    num_of_turtles = screen.numinput(title='num_of_turtles', prompt='How many turtles do you want to race?')
    all_turtles = []
    field_height = 200
    turtle_spacing = field_height / int(num_of_turtles)

    for index in range(0, int(num_of_turtles)):
        turtle = Turtle(shape='turtle')
        turtle.turtlesize(0.5)
        turtle.penup()
        turtle.color(rand_rgb())
        new_y = (field_height / 2) - (turtle_spacing * index)
        turtle.goto(x=-230, y=new_y)
        turtle.write(index + 1, align='left')
        all_turtles.append(turtle)

    user_bet = screen.numinput(title='lucky turtle?', prompt='Which turtle do you think will win?')

    if user_bet:
        race_is_on = True

    while race_is_on:
        random_turtle_num = randint(0, num_of_turtles - 1)
        rand_distance = randint(0, 20)
        all_turtles[random_turtle_num].forward(rand_distance)
        turtle_number = 0
        for turtle in all_turtles:
            turtle_number += 1
            if turtle.pos()[0] > 230:
                race_is_on = False
                print(f'Turtle number {turtle_number} won!')
                if user_bet == turtle_number:
                    reply = screen.textinput(title=f'Turtle {turtle_number} won!',
                                             prompt='You win! Would you like to play again, Y or N')
                else:
                    reply = screen.textinput(title=f'Turtle {turtle_number} won!',
                                             prompt='You lose! Would you like to play again, Y or N')

    if reply.lower() == 'n':
        play_again = False
    else:
        screen.clearscreen()

screen.bye()
# from turtle import Turtle, Screen
# from random import randint
#
# screen = Screen()
# screen.setup(width=500, height=400)
# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
# names = ['tim0', 'tim1', 'tim2', 'tim3', 'tim4', 'tim5']
# all_turtles = []
# is_race_on = False
#
#
# def make_turtle(name, color, pos):
#     name = Turtle(shape='turtle')
#     name.color(color)
#     name.penup()
#     new_pos = 60 - (20 * index)
#     name.goto(x=-230, y=new_pos)
#     all_turtles.append(name)
#
#
# for index in range(0, len(names)):
#     make_turtle(names[index], colors[index], index)
#
# user_bet = screen.textinput('Which turtle will win the race?', prompt='Enter a color.')
#
# if user_bet:
#     is_race_on = True
#
# while is_race_on:
#     rand_dist = randint(0, 10)
#     rand_index = randint(0, 5)
#     all_turtles[rand_index].forward(rand_dist)
#     for turtle in all_turtles:
#         if int(turtle.pos()[0]) > 220:
#             is_race_on = False
#             winning_color = turtle.fillcolor()
#             turtle.write('I Win!')
#             for num in all_turtles:
#                 if num.fillcolor() != winning_color:
#                     num.color('black')
#             if user_bet == winning_color:
#                 print(f'You won! {winning_color.title()} won the race!')
#             else:
#                 print(f'You lost! {winning_color.title()} won the race!')
#
# screen.exitonclick()
