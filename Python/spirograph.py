from turtle import Turtle, Screen
import turtle
import random

tim = Turtle()
tim.shape("turtle")
turtle.colormode(255) #throwing error? uncomment this line to run.


def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_colour())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(10)


screen = Screen()
screen.exitonclick()
