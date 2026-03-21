import turtle as t
import random
tim = t.Turtle()

t.colormode(255)
def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

def draw_circle(gap_size):
    for i in range(int(360 / gap_size)):
        tim.circle(100)
        tim.speed("fastest")
        tim.color(random_colour())
        tim.setheading(tim.heading() + gap_size)

draw_circle(10)
screen = t.Screen()
screen.exitonclick()
