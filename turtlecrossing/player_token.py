from turtle import Turtle
import scoreboard



class PlayerToken(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.penup()
        self.goto(x=0, y=-280)

    def up(self):
        current_y = self.ycor()
        new_y = current_y + 20
        self.goto(x=self.xcor(), y=new_y)


    def down(self):
        current_y = self.ycor()
        new_y = current_y - 20
        self.goto(x=self.xcor(), y=new_y)

    def left(self):
        current_x = self.xcor()
        new_x = current_x - 20
        self.goto(x=new_x, y=self.ycor())

    def right(self):
        current_x = self.xcor()
        new_x = current_x + 20
        self.goto(x=new_x, y=self.ycor())
