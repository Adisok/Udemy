from tkinter import *
import pandas as pd
from random import choice
BACKGROUND_COLOR = "#B1DDC6"
FONT = "Arial"
global flip, word_random

# https://app.memrise.com/course/403692/russian-1000-words-audio-wykoppl/


def next_card():
    global flip, word_random

    window.after_cancel(flip)

    word_random = choice(list(words_dict.keys()))
    canvas.itemconfig(card, image=front_card)
    canvas.itemconfig(word, text=word_random,  fill="black")
    canvas.itemconfig(language, text="Russian",  fill="black")

    flip = window.after(3000, func=flip_card)


def known_word():
    del words_dict[word_random]

    data = {"Russian": words_dict.keys(), "Polish": words_dict.values()}
    data_csv = pd.DataFrame.from_dict(data)
    data_csv.to_csv("./data/words_to_learn.csv")
    next_card()


def flip_card():
    global word_random

    canvas.itemconfig(card, image=back_card)
    canvas.itemconfig(language, text="Polish")
    canvas.itemconfig(word, text=words_dict[word_random], fill="white")


# pandas
try:
    data_pandas = pd.read_csv("./data/words_to_learn.csv")
    words_dict = {value.Russian: value.Polish for (index, value) in data_pandas.iterrows()}
except FileNotFoundError:
    data_pandas = pd.read_csv("./data/russian.csv")
    words_dict = {value.Russian: value.Polish for (index, value) in data_pandas.iterrows()}
    print(data_pandas)

# to_learn = pd.data_pandas.to_dict(orient="records")
window = Tk()
window.minsize(width=900, height=600)
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip = window.after(3000, func=flip_card)

# Canvas
front_card = PhotoImage(file="./images/card_front.png")
back_card = PhotoImage(file="./images/card_back.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card = canvas.create_image(400, 262, image=front_card)
canvas.grid(row=0, column=0, columnspan=2)
language = canvas.create_text(400, 150, text="Language", font=(FONT, 40, "italic"))
word = canvas.create_text(400, 262, text="Word", font=(FONT, 60, "bold"))

# buttons
next_card()
ok_image = PhotoImage(file="./images/right.png")
ok_button = Button(image=ok_image, highlightthickness=0, command=known_word)
ok_button.grid(row=1, column=1)

bad_image = PhotoImage(file="./images/wrong.png")
bad_button = Button(image=bad_image, highlightthickness=0, command=next_card)
bad_button.grid(row=1, column=0)

window.mainloop()
