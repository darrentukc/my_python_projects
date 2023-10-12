from turtle import Turtle, Screen

screen = Screen()
turtle_list = []
game = True

for index in range(0,3):
    turtle = Turtle()
    turtle.goto(x=0, y=(index*10))
    turtle.setheading(90)
    turtle_list.append(turtle)

for item in turtle_list:
    print(item)
    item.forward(10)


screen.exitonclick()