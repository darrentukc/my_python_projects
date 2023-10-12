from turtle import Turtle, Screen

# FIELD_WIDTH = 1000
# FIELD_HEIGHT = 600

class PlayField:

    def __init__(self, field_width, field_height):
        self.screen = Screen()
        self.screen.bgcolor('black')
        self.screen.setup(width=field_width, height=field_height)
        self.screen.title('Pong')
        self.fieldline = Turtle()
        self.fieldline.color('white')
        self.fieldline.speed('fastest')
        self.fieldline.penup()
        self.fieldline.goto(x=0, y=290)
        self.fieldline.setheading(270)
        self.fieldline.hideturtle()
        for space in range(int(field_height / 40)):
            self.fieldline.pendown()
            self.fieldline.forward(20)
            self.fieldline.penup()
            self.fieldline.forward(20)


