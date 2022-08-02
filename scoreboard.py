FONT = ("Courier", 20, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-220,250)
        self.update_score()


    def update_score(self):
        self.write(f"Level {self.level}", align="center", font=FONT)

    def increase_level(self):
        self.level+=1
        self.clear()
        self.update_score()




