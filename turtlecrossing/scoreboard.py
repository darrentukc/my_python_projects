from turtle import Turtle, Screen


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.hideturtle()
        self.penup()
        self.goto(x=-200, y=220)
        self.current_level = 1
        self.refresh()

    def next_level(self):
        self.current_level += 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f'Level: {self.current_level}', align='center', font=('Arial', 40, 'normal'))

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg='game over', align='center', font=('Arial', 40, 'normal'))
