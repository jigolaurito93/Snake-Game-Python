from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create a snake body
snake = Snake()

# Activate the event listener
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

# Create a food object
food = Food()

scoreboard = Scoreboard()

# Move the snake forward
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        # If snake collides with food, food location relocates
        food.refresh()
        # Adds tail extension to snake body
        snake.extend()
        scoreboard.increase_score()
    
    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        # Displays GAMEOVER when the snake hits the wall
        scoreboard.game_over()
    
    # Detect collision with tail
    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


    
    





# Detect collision with food
screen.exitonclick()