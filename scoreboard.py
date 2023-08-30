from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()
        self.hideturtle()

    # Updates the current score on the scoreboard
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
    
    # Method that displays GAMEOVER when the snake hits the wall
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAMEOVER!", align=ALIGNMENT, font=FONT)

    
    def increase_score(self):
        self.score += 1
        # Clears the previous text that was written by the turtle
        self.clear()
        self.update_scoreboard()
