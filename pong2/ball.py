from turtle import Turtle

class Ball(Turtle):
    def __init__(self, angle):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.setheading(45)
        self.penup()
        self.speed('normal')
        self.goto(x=0, y=0)


    def move(self, speed):
        self.forward(speed)

    def wall_bounce(self):
        if self.heading() == 45:
            self.setheading(315)
        elif self.heading() == 315:
            self.setheading(45)
        elif self.heading() == 135:
            self.setheading(225)
        elif self.heading() == 225:
            self.setheading(135)

    def paddle_bounce(self):
        if self.heading() == 45:
            self.setheading(135)
        elif self.heading() == 315:
            self.setheading(225)
        elif self.heading() == 135:
            self.setheading(45)
        elif self.heading() == 225:
            self.setheading(315)

    def restart(self):
        self.goto(x=0, y=0)
