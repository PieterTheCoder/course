from turtle import Turtle, Screen
import pandas

screen = Screen()
turtle = Turtle()
image = "blank_states_img.gif"

data = pandas.read_csv("50_states.csv")
screen.title("U. S. States Game")
screen.addshape(image)
turtle.shape(image)
all_state = data["state"].to_list()
score = 0
guessed_state = []

while len(guessed_state) < 50:
    answer = screen.textinput(title="", prompt=f"{len(guessed_state)}/50 States Correct").title()
    # if answer == "Exit":
    #     nonguessed_state = []
    #     for state in all_state:
    #         if state not in guessed_state:
    #             nonguessed_state.append(state)
    #     new_data = pandas.DataFrame(nonguessed_state)
    #     new_data.to_csv("states_to_learn.csv")
    #     break
    if answer == "Exit":
        missing_state = [state for state in all_state if state not in guessed_state]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer in all_state:
        score += 1
        guessed_state.append(answer)
        t = Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer)

