from turtle import Turtle
from Paddle import Paddle


class Brick(Turtle):
    def __init__(self, position):
        super().__init__()
        self.goto(position)
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=7)
        self.penup()








