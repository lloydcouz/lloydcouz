import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(key='Up', fun=player.move)

cars = []

for i in range(0, 25):
    car = CarManager()
    cars.append(car)

scoreboard = Scoreboard()

car_speed = 0.1

game_is_on = True
while game_is_on:
    time.sleep(car_speed)
    screen.update()

    # moves all the initial cars
    for i in cars:
        i.move()
        if i.xcor() < -320:
            i.reset_car()
        if player.distance(i) < 20:
            game_is_on = False
            scoreboard.game_over()

    # new level
    if player.ycor() > 230:
        scoreboard.next_level()
        player.goto((0, -280))
        car_speed *= 0.5
        time.sleep(car_speed)



screen.exitonclick()