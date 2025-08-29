from turtle import Turtle
FONTS =("courier",20,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-270,270)
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level : {self.level}", align="left", font=FONTS)
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONTS)