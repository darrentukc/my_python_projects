from turtle import Turtle

class Ball(Turtle):

    def __init__(self, field_width, field_height):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.setheading(20)
        self.penup()
        self.move()
        field_width = field_width
        field_height = field_height


    def move(self):
        self.forward(10)
        # if self.pos()[1] > field_height / 2:



