from turtle import Turtle, Screen


class MeatBoy(Turtle):
    def __init__(self, screenwidth, screenheight):
        super().__init__()
        self.shape()
        self.color('firebrick')
        self.penup()
        self.goto(x=(screenwidth / -4), y=0)
        self.acceleration = 10
        self.screen = Screen()

    def accel(self):
        if self.acceleration < 10:
            self.acceleration += 1
        else:
            pass

    def accel_release(self):
        while self.acceleration > 0:
            self.forward(self.acceleration)
            self.acceleration -= 2
            self.screen.update()
            print(self.acceleration)


    def move_right(self):
        self.setheading(0)
        self.accel()
        self.forward(self.acceleration)
        print(self.acceleration)

    def move_left(self):
        self.setheading(180)
        self.accel()
        self.forward(self.acceleration)

    def momentum(self):
        pass
