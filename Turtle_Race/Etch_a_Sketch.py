from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()
def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(00)
def move_left():
    tim.left(10)

def move_right():
    tim.right(10)
def clean_up():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(clean_up, "space")
screen.exitonclick()
