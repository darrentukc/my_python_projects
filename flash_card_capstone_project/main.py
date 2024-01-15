import random
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


# ---------------------------- FUNCTION ------------------------------- #


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_card['French'], fill='black')
    canvas.itemconfig(card_image, image=card_front_image)
    # words_to_learn.remove(random_word)
    # df_to_save = pd.DataFrame(words_to_learn)
    # df_to_save.to_csv('data/words_to_learn.csv')
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(card_image, image=card_back_image)


def is_known():
    to_learn.remove(current_card)
    next_card()
    data = pd.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)


# ---------------------------- UI SETUP ------------------------------- #

# window

window = Tk()
window.title('Flash Cards')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, func=flip_card)

check_img = PhotoImage(file="images/right.png")
cross_img = PhotoImage(file="images/wrong.png")
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=529, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 264, image=card_front_image)
card_title = canvas.create_text(400, 150, font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 256, font=('Ariel', 40, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

# Button Field

unknown_button = Button(image=cross_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

known_button = Button(image=check_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

# ---------------------------- WORD DB SETUP ------------------------------- #

try:
    df = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    df = pd.read_csv('data/french_words.csv')
    to_learn = df.to_dict(orient='records')
else:
    to_learn = df.to_dict(orient='records')

next_card()

window.mainloop()
