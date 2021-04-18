import turtle
import pandas as pd
from time import sleep

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")

names = data.state.to_list()
# x_cor = data.x.to_list()
# y_cor = data.y.to_list()

name_on_map = turtle.Turtle()
name_on_map.penup()
name_on_map.ht()
name_on_map.color("black")

score = 0
guessed = []

while score < 50:
    answer_state = screen.textinput(title=f"{score}/{len(names)} Guess the State", prompt="What's another state's name? ").title()

    if answer_state in names and answer_state not in guessed:
        guessed.append(answer_state)
        score += 1
        name_on_map.goto(int(data.x[data.state == answer_state]), int(data.y[data.state == answer_state]))
        name_on_map.write(f"{answer_state}")
    elif answer_state == "Exit":
        not_guessed = [n for n in names if n not in guessed]
        # not guessed states
        not_guessed_csv = pd.DataFrame(not_guessed)
        not_guessed_csv.to_csv("Not_Guessed.csv")
        break




