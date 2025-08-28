from turtle import Turtle
import random
import turtle
color = ["red", "green", "blue", "yellow", "orange", "purple"]
y_positions = [-90,-60,-30,0,30,60,]
all_turtles = []
screen = turtle.Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Turtle_Race", prompt="Which turtle will win the race?\nEnter a color(lowercase) : \n")
for turtle_index in range(0,6):
    new_turtle = Turtle("turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color =turtle.pencolor()
            if winning_color == user_bet:
                print(f"You Win! {winning_color} is the winner!")
            else:
                print(f"You Lose! {winning_color} is the winner!")
        random_distance = random.randint(1,10)
        turtle .forward(random_distance)
screen.exitonclick()