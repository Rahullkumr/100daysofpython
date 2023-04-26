from turtle import Turtle
import random


class Ground(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.goto(0, -265)
        self.color("gray")
        self.shapesize(stretch_len=30, stretch_wid=2.7)
        self.colors = [
            "red", "yellow", "blue", "magenta","maroon", "gold", "olive",  "purple", "wheat",
            "peru", "orange", "green", "pink", "indigo", "tomato", "lime", "cyan",
        ]

    def change_color(self):
        self.color(random.choice(self.colors))
