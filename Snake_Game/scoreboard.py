from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        with open("data.txt", "r") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.color("White")
        self.update_scoreboard()


        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()