from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, start_position):
        self.start_position = start_position
        self.x_pointer_pos = 0
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=7)
        self.penup()
        self.goto(self.start_position)

    def get_position(self, event):
        self.x_pointer_pos = event.x

    def move(self, event):
        self.get_position(event)

        # self.goto(self.x_pointer_pos-400, self.start_position[1])
        self.setx(self.x_pointer_pos-400)
        self.sety(self.start_position[1])
