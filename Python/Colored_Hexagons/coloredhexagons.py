import turtle
from random import randint
#x for the expected circle value 1
x = 20
#variable for the expected muller circle 2
muller = 20
#the speed of the pen value 3 
turtle.speed(100)
# the turtle colormode set to 255
turtle.colormode(255)
#the move function
def move(l, a):
                turtle.right(a)
                turtle.forward(l)
#the hex function
def hex():
        turtle.pendown()
        turtle.color( randint(0,255),randint(0,255),randint(0,255) )
        turtle.begin_fill()
        for i in range(6):
                move(x,-60)
        turtle.end_fill()
        turtle.penup()

# start the drawing
turtle.penup()
#loop that draws the number of pentagons.
for max in range (muller):
        if max == 0:
                hex()
                move(x,-60)
                move(x,-60)
                move(x,-60)
                move(0,180)
        for i in range (6):
                move(0,60)
                for j in range (max+1):
                        hex()
                        move(x,-60)
                        move(x,60)
                move(-x,0)
        move(-x,60)
        move(x,-120)
        move(0,60)
#this function runs the code until the mouse is clicked
turtle.exitonclick()

# By: Max Müller
 