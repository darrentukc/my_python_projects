from turtle import Turtle
from random import randint, randrange

list_of_colors = ['red', 'yellow', 'orange', 'purple', 'green', 'blue']
list_of_cars = []





class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color(list_of_colors[randint(0, 5)])
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.setheading(180)
        rand_x = randint(-200, 280)
        rand_y = randint(-200, 200)
        self.goto(x=rand_x, y=rand_y)
        self.movespeed = randrange(20, 30, 5)
        list_of_cars.append(self)

    def move(self):
        for item in list_of_cars:
            item.forward(item.movespeed)
            if item.xcor() < -300:
                item.goto(x=300, y=item.ycor())

    def check_collision(self, player_token):
        for item in list_of_cars:
            if -20 < item.xcor() < 20 and player_token.ycor() - 20 < item.ycor() < player_token.ycor() + 20:
                return True