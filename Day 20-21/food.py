from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        random_X = random.randint(-270, 270)
        random_Y = random.randint(-270, 270)
        self.goto(random_X, random_Y)
        self.refresh()

    def refresh(self):
        random_X = random.randint(-270, 270)
        random_Y = random.randint(-270, 270)
        self.goto(random_X, random_Y)