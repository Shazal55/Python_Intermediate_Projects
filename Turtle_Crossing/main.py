from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("sky blue")
screen.title("Turtle Crossroad")
screen.tracer(0)
game_is_on = True
player = Player()
car_manager= CarManager()
scoreboard =Scoreboard()
screen.listen()
screen.onkeypress(player.move_down, "Down")
screen.onkeypress(player.move_up, "Up")
while game_is_on:
    screen.update()
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(player)<25:
            game_is_on = False
            scoreboard.game_over()
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
screen.exitonclick()