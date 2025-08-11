from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()
ball.speed("fast")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

game_is_on = True


screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
#Detect collision with ball
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
#Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.hit()
#detect when right paddle misses
    if ball.xcor()>380:
        ball.restart()
        scoreboard.l_point()
    if ball.xcor()<-380:
        ball.restart()
        scoreboard.r_point()
screen.exitonclick()
