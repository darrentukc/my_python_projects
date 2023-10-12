from turtle import Turtle
from time import sleep

class ComputerPaddle:
    def __init__(self, field_width, field_height):
        self.computer_paddle_list = []
        self.field_width = field_width
        self.field_height = field_height


    def create(self, paddle_size):
        for index in range(0, paddle_size):
            self.paddle = Turtle(shape='square')
            self.paddle.color('white')
            self.paddle.penup()
            self.paddle.setheading(90)
            self.paddle.speed('fastest')
            self.paddle.goto(x=(self.field_width / 2) - 15, y=index * 20)
            self.computer_paddle_list.append(self.paddle)

    def move(self, computer_speed):
        for item in self.computer_paddle_list:
            item.forward(10)
        if self.computer_paddle_list[-1].ycor() == self.field_height/2:
            for item in self.computer_paddle_list:
                item.setheading(270)
        elif self.computer_paddle_list[0].ycor() == (self.field_height/-2):
            for item in self.computer_paddle_list:
                item.setheading(90)
        sleep(computer_speed)

