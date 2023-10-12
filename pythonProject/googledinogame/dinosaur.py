from turtle import Turtle
from time import sleep

class Dino(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)

    def jump(self):
        if self.ycor() == 0:
            self.forward(100)
            sleep(0.3)
            self.backward(100)
        else:
            pass