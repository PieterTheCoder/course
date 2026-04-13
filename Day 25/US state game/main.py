from turtle import Turtle, Screen
import pandas

screen = Screen()
turtle = Turtle()
image = "blank_states_img.gif"

data = pandas.read_csv("50_states.csv")
write_state = turtle()
write_state.penup()
write_state.hideturtle()
screen.title("U. S. States Game")
screen.addshape(image)
turtle.shape(image)
all_state = data["state"].to_list()
x_states = data["x"].to_list()
y_states = data["y"].to_list()
# alabama = data[data.state == "Alabama"]

answer = screen.textinput(title="Guess the state", prompt="What's another state name?").upper()
if answer == all_state:
    pass
print(answer)


screen.exitonclick()