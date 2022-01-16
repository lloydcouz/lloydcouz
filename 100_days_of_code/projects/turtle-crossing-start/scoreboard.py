FONT = ("Courier", 24, "normal")

from player import Player
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color('black')
        self.goto((-250, 270))
        self.write(f'Level: {self.level}', align='left', font=FONT)
        self.finish_line()

    def next_level(self):
        self.level += 1
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto((-250, 270))
        self.write(f'Level: {self.level}', align='left', font=FONT)
        self.finish_line()

    def finish_line(self):
        self.penup()
        self.hideturtle()
        self.color('black')
        self.pensize(2)
        self.goto((300, 250))
        self.pendown()
        self.goto(-300, 250)

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write(f'Game over! You made it to Level: {self.level}', align='center', font=("Courier", 24, "bold"))
