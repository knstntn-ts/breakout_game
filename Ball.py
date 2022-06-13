from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto((0, 0))
        self.xmove = 1
        self.ymove = 1
        self.speed(100)


    def move(self):
        new_y = self.ycor() - self.ymove
        new_x = self.xcor() + self.xmove

        # self.goto(new_x, new_y)

        self.setx(new_x)
        self.sety(new_y)

    def ybounce(self):

        self.ymove = -1 * self.ymove

    def xbounce(self):
        self.xmove *= -1.0

    def reset_position(self):
        self.goto(0, 0)
        self.xmove *= -1
