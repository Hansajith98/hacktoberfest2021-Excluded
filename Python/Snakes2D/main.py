# FONT_TUPPLE=("Arial",8,"normal")

import turtle
from snakes import Snake
from turtle import Turtle,Screen
from food import Food
import time
from scoreboard import ScoreBoard
screen=Screen()
snake=Snake(3)
snakes_food=Food()
race_is_on=True
screen.setup(width=600,height=700)
screen.bgcolor("black")
screen.title("Snakes 2D")
screen.tracer(0)
screen.listen()
score=ScoreBoard()
# used to remove the trace


screen.onkey(snake.snake_up,"Up")
screen.onkey(snake.snake_down,"Down")
screen.onkey(snake.snake_left,"Left")
screen.onkey(snake.snake_right,"Right")


snake.create_snake()

while race_is_on:
    screen.update()
    time.sleep(0.2)

    snake.move()

    if snake.snake_head.distance(snakes_food)<15:
        score.update_score()
        snakes_food.refresh_food_pos()
        snake.extend()

    if snake.snake_head.xcor() > 285 or snake.snake_head.xcor() < -285 or snake.snake_head.ycor() < -340 or snake.snake_head.ycor() > 340:
        score.game_over()
        race_is_on=False


    for segment_need_to_be_checked in snake.segments[1:len(snake.segments)]:
        if snake.snake_head.distance(segment_need_to_be_checked) < 10 :
            score.game_over()
            race_is_on=False

screen.exitonclick()