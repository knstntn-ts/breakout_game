from turtle import Screen, Turtle
import Ball
import Paddle
import Bricks

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Breakout Game")
screen.tracer(0)

game_is_on = True

# Initialization
paddle = Paddle.Paddle((0, -250))
my_ball = Ball.Ball()
# put the bricks on the screen
bricks = {}
cnt = 0
for j in range(3):
    for i in range(4):
        bricks.update({cnt: Bricks.Brick([i * 200 - 300, 75 + j * 75])})
        cnt += 1

# Displays the score
sketch = Turtle()
sketch.speed(0)
sketch.color("white")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Score : 0", align="center", font=("Courier", 24, "normal"))

# Used to track position of the mouse
pointer = screen.getcanvas()
pointer.bind('<Motion>', paddle.move)

# margin for detecting collisions with bricks and paddle
margin_x = 50

# score variable
score = 0
while game_is_on:
    screen.update()

    ### Collisions with the walls
    # Detect collision with the side walls
    if my_ball.xcor() > 380 or my_ball.xcor() < -380:
        my_ball.xbounce()
    # Detect collision with the upper wall
    if my_ball.ycor() > 280:
        my_ball.ybounce()
    # Detect collision with the bottom wall
    if my_ball.ycor() < -290:
        game_is_on = False

    # Detect collision with the paddle
    if -240 > my_ball.ycor() > -250 and paddle.xcor()+margin_x > my_ball.xcor() > paddle.xcor()-margin_x:
        my_ball.sety(paddle.ycor()+20)
        my_ball.ybounce()

    # Detect collision with bricks
    for i in bricks.keys():
        if bricks.get(i):
            if bricks[i].ycor()+10 > my_ball.ycor() > bricks[i].ycor()-10 and \
                    bricks[i].xcor()+margin_x > my_ball.xcor() > bricks[i].xcor()-margin_x:
                score += 1
                sketch.clear()
                sketch.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
                my_ball.sety(bricks[i].ycor() + 5)
                my_ball.ybounce()
                bricks[i].reset() # to remove the white square
                bricks.pop(i) # pop from the dictionary
                break # to exit for loop, otherwise gives an error that dictionary changed during iteration

    # if there are no more bricks left stop the game
    if len(bricks) == 0:
        game_is_on = False
        sketch.clear()
        sketch.write("You final score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    my_ball.move()

screen.exitonclick()