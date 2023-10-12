from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.pad = Turtle()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.penup()
        self.goto(x=position[0], y=position[1])

    def go_up(self):
        new_y = int(self.ycor()) + 20
        self.goto(x=self.xcor(), y=new_y)

    def go_down(self):
        new_y = int(self.ycor()) - 20
        self.goto(x=self.xcor(), y=new_y)