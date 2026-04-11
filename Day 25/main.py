from turtle import Turtle, Screen
import pandas

screen = Screen()
turtle = Turtle()
image = "blank_states_img.gif"

screen.title("U. S. States Game")
screen.addshape(image)
turtle.shape(image)

answer = screen.textinput(title="Guess the state", prompt="What's another state name?")
print(answer)

screen.exitonclick()