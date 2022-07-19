from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, start_position):
        # --- INITIALIZE THE PADDLE --- #

        self.start_position = start_position
        self.x_pointer_pos = 0
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=7)
        self.penup()
        self.goto(self.start_position)

    # Get location of a paddle to use for ball
    def get_position(self, event):
        self.x_pointer_pos = event.x

    # Moving the paddle
    def move(self, event):
        self.get_position(event)
        self.setx(self.x_pointer_pos-400)
        self.sety(self.start_position[1])
