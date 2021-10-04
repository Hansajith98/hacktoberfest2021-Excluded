import turtle

MOVE_DISTANCE=20
UP=90.0
DOWN=270.0
RIGHT=0.0
LEFT=180.0

class Snake:
    def __init__(self,size):
        self.size=size
        self.segments=[]
        self.cordinates=[(-20,0),(-40,0),(-60,0),(-80,0)]



    def create_snake(self):
        for turtL in range(0,self.size):
            tim = turtle.Turtle(shape="square")
            tim.penup()
            # tim.shape("square")
            tim.color("white")
            tim.goto(self.cordinates[turtL])
            self.segments.append(tim)
            self.snake_head =self.segments[0]



    def add_turtle(self,turtl):
        tim = turtle.Turtle(shape="square")
        tim.penup()
        # tim.shape("square")
        tim.color("white")
        tim.goto(turtl)
        self.segments.append(tim)




    def extend(self):
        self.add_turtle(self.segments[-1].position())


    def move(self):
        for segment_mark in range(len(self.segments) - 1, 0, -1):
            x = self.segments[segment_mark - 1].xcor()
            y = self.segments[segment_mark - 1].ycor()
            self.segments[segment_mark].goto(x, y)

        self.segments[0].forward(MOVE_DISTANCE)

        # self.segments[0].left(90)

    def snake_up(self):
        if self.segments[0].heading()!=DOWN:
            self.segments[0].setheading(UP)

    def snake_down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def snake_right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def snake_left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)