from turtle import Turtle
from random import randint

class Obstacles():
    def __init__(self):
        self.obstacle_list = []

    def create(self):
        x = randint(1,20)
        rand_height = randint(1,5)
        if x == 1:
            self.new = Turtle(shape='square')
            self.new.hideturtle()
            self.new.penup()
            self.new.goto(x=400, y=((rand_height*10)-10))
            self.new.showturtle()
            self.new.shapesize(stretch_wid=rand_height, stretch_len=1)
            self.obstacle_list.append(self.new)




    def move(self):
        for obstacle in self.obstacle_list:
            new_x = obstacle.xcor() - 20
            obstacle.goto(x=new_x, y=obstacle.ycor())
            if obstacle.xcor() < -500:
                self.obstacle_list.remove(obstacle)