from turtle import Turtle
from snake import Snake
import os
import subprocess
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def restart_game(self):

        subprocess.run(["python" ,"main.py"])
        quit()



    def game_over(self):
        self.goto(0,0)
        self.write("Game over! Want to restart the game? Y or N", align=ALIGNMENT, font=FONT)
        answer = input("Y or N?")
        if answer == "Y":
            self.restart_game()
            quit()
        else:
            quit()



