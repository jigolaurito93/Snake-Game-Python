from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create a snake body
snake = Snake()

# Move the snake forward
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    
    






screen.exitonclick()