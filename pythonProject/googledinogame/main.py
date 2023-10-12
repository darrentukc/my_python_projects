from turtle import Screen
from dinosaur import Dino
from obstacles import Obstacles

FIELDHEIGHT = 400
FIELDWIDTH = 1000


screen = Screen()
screen.setup(width=FIELDWIDTH, height=FIELDHEIGHT)

dino = Dino()
obstacle = Obstacles()
# screen.tracer(0)

screen.listen()
screen.onkeypress(dino.jump, key='w')
screen.onkeypress(obstacle.create, key='s')


game_is_on = True
while game_is_on:
    obstacle.create()
    obstacle.move()
    # screen.update()

screen.exitonclick()