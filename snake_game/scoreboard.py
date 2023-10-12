from turtle import Turtle

X_POS = 0
Y_POS = 260
ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(X_POS, Y_POS)
        self.color('white')
        self.current_score = 0
        self.refresh()
        self.ht()

    def add_score(self):
        self.current_score += 1
        self.clear()
        self.refresh()

    def refresh(self):
        self.write(arg=f'Score: {self.current_score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg='GAME OVER!', align=ALIGNMENT, font=FONT)
