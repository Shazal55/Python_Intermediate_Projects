from turtle import Turtle
FINISH_LINE_Y = 280
STARING_POSITION = (0,-280)
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.go_to_start()
    def move_up(self):
        new_y =self.ycor()+10
        self.goto(self.xcor(),new_y)
    def move_down(self):
        new_y = self.ycor()-10
        self.goto(self.xcor(),new_y)
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
    def go_to_start(self):
        self.goto(STARING_POSITION)