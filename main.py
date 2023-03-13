import time
from turtle import Screen
from player import Player
from carmanager import Carmanager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
tim = Player()
carmanager = Carmanager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(tim.move, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    carmanager.create_cars()
    carmanager.move_cars()

    for car in carmanager.all_cars:
        if car.distance(tim) < 20:
            game_is_on = False
            scoreboard.game_over()

    if tim.is_at_finish_line():
        tim.go_to_start()
        carmanager.level_up()
        scoreboard.increase_level()
screen.exitonclick()