from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(x=-280, y=250)
        self.update_scoreboard()


    def increase_level(self):
        self.clear()
        self.level += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Level: {self.level}', align='left', font=FONT)


    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over!', align='center', font=FONT)
