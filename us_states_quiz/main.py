import turtle
from scoreboard import ScoreBoard
import pandas as pd

image = 'day-25-us-states-game-start/blank_states_img.gif'
screen = turtle.Screen()
screen.title('U.S. State Quiz')
screen.addshape(image)
turtle.shape(image)


df = pd.read_csv('day-25-us-states-game-start/50_states.csv')
state_list = df['state'].tolist()
list_of_answers = []

score_board = ScoreBoard()


game_is_on = True
while game_is_on:
    answer_state = (screen.textinput(title=f'{score_board.score} / 50 correct', prompt='what is your answer')).title()

    states_to_learn = [x for x in state_list if x not in list_of_answers]

    if answer_state == 'Exit':
        states_to_learn = [x for x in state_list if x not in list_of_answers]
        new_df = pd.DataFrame(states_to_learn)
        new_df.to_csv('states_to_learn')
        break

    elif answer_state in state_list and answer_state not in list_of_answers:
        # create turtle
        state = turtle.Turtle()
        state.hideturtle()
        state.penup()

        # get x cor and y cor from df
        xcor = df[df['state'] == answer_state]['x'].iloc[0]
        ycor = df[df['state'] == answer_state]['y'].iloc[0]

        # send turtle to coordinates and write state name
        state.goto(x=xcor, y=ycor)
        state.write(answer_state, align='center')

        # add answer to list of answers
        list_of_answers.append(answer_state)

        # add score
        score_board.add_score()
