from turtle import Turtle, Screen

# Create a snake body
starting_positions = [(0,0), (-20,0), (-40,0)]

for position in starting_positions:
    new_segment = Turtle()
    new_segment.shape("square")
    new_segment.color('white')
    new_segment.goto(position)




screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.exitonclick()