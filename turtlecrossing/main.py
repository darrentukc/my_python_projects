from turtle import Screen
from player_token import PlayerToken
from cars import Car
from time import sleep
from scoreboard import ScoreBoard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
level = 1  # 0 - 4
NUM_OF_CARS = (level * 2) + 5
new_cars = True
sleep_time = 0.1

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)
token = PlayerToken()
score_board = ScoreBoard()
game_is_on = True

screen.listen()
screen.onkey(token.up, key='Up')
screen.onkey(token.down, key='Down')
screen.onkey(token.left, key='Left')
screen.onkey(token.right, key='Right')

while game_is_on:
    sleep(sleep_time)

    # adds more cars if user increased level previously
    if new_cars:
        for index in range(NUM_OF_CARS):
            car = Car()
        new_cars = False

    # moves cars/obstacles on screen
    car.move()

    # checks if player/token collides with car
    if car.check_collision(token):
        game_is_on = False
        score_board.game_over()

    # checks to see if token reached the top of screen, returns to start and adds level
    if token.ycor() == 280:
        score_board.next_level()
        token.goto(x=0, y=-280)
        new_cars = True
        # sleep_time = sleep_time / 1.5

    # updates screen
    screen.update()

screen.exitonclick()
