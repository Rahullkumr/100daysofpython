from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.y_move = 1
        self.is_bouncing = True
        self.goto(0, 200)
        self.shape("circle")
        self.shapesize(stretch_len=2.5, stretch_wid=2.5)

    def fall(self):
        new_y = self.ycor() - self.y_move
        self.goto(0, new_y)

    def change_mvmt_dir(self):
        self.y_move *= -1

