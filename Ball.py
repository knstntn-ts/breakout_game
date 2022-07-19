from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        # --- INITIALIZE THE BALL --- #

        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto((0, 0))
        self.xmove = 1
        self.ymove = 1
        self.speed(100)

    # Move the ball
    def move(self):
        new_y = self.ycor() - self.ymove
        new_x = self.xcor() + self.xmove
        self.setx(new_x)
        self.sety(new_y)

    # Bouncing functions
    def ybounce(self):
        self.ymove = -1 * self.ymove

    def xbounce(self):
        self.xmove *= -1.0

    # Resetting the ball when it is out of bounce
    def reset_position(self):
        self.goto(0, 0)
        self.xmove *= -1
