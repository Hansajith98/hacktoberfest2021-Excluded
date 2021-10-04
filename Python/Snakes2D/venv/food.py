from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
       super().__init__()
       self.shape("circle")
       self.color("blue")
       self.penup()
       self.shapesize(stretch_wid=0.4,stretch_len=0.4)
       self.speed("fastest")
       self.refresh_food_pos()

    def refresh_food_pos(self):
       random_x=random.randint(-280,280)
       random_y=random.randint(-330,330)
       self.goto(random_x,random_y)