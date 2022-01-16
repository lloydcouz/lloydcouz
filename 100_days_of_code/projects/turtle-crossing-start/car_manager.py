COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

from turtle import Turtle
from random import randint, choice


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color(choice(COLORS))
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.goto(x=randint(-300, 250), y=randint(-200, 230))
        self.car_speed = STARTING_MOVE_DISTANCE

    def move(self):
        self.backward(self.car_speed)

    def reset_car(self):
        self.hideturtle()
        self.goto(randint(320, 400), randint(-250, 250))
        self.color(choice(COLORS))
        self.showturtle()
        self.move()

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
