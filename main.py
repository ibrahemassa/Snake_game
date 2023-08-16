from turtle import Screen
from snake import Snake
from food import Food
from score import ScoreBoard
import random
import time


my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Snake")
my_screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")

is_on = True
while is_on:
    my_screen.update()
    time.sleep(0.07)
    snake.move()
    if snake.wall():
        score.reset()
        snake.reset()
    # collide = snake.collide_tail()

    # if collide:
    #     is_on = False

    if snake.head.distance(food) < 15:
        food.new_location()
        score.increse_score()
        snake.extend()

    for piece in snake.snake[1:]:
        if snake.head.distance(piece) <= 10:
            score.reset()
            snake.reset()


my_screen.exitonclick()