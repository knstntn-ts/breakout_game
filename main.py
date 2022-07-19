##### IMPORT STATEMENTS
from turtle import Screen, Turtle
import Ball
import Paddle
import Bricks

##### GAME VARIABLES
# score variable
score = 0
# lives
lives = 3

# --- Initialization --- #
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Breakout Game")
screen.tracer(0)

game_is_on = True

# --- SETUP OF GAME ELEMENTS --- #
paddle = Paddle.Paddle((0, -250))
my_ball = Ball.Ball()
# Bricks are saved in a dictionary with 'cnt' as their id for reference in the code
# Put the bricks on the screen, 3 rows and 4 columns
bricks = {}
cnt = 0
for j in range(3):
    for i in range(4):
        bricks.update({cnt: Bricks.Brick([i * 200 - 300, 75 + j * 75])})
        cnt += 1

# --- DISPLAY SETUP --- #
sketch = Turtle()
sketch.speed(0)
sketch.color("white")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Score: {}. Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

# Used to track position of the mouse
pointer = screen.getcanvas()
pointer.bind('<Motion>', paddle.move)

# margin for detecting collisions with bricks and the ball
margin_x = 50

# --- GAME LOOP --- #
while game_is_on:
    # Update the screen to see if there are any changes.
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
        # In this case the ball is out, so minus one life.
        lives -= 1
        my_ball.reset_position()
        sketch.clear()
        sketch.write("Score: {}. Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))
        if lives == 0:
            # End the game if no more lives
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
                sketch.write("Score: {}. Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))
                my_ball.sety(bricks[i].ycor() + 5)
                my_ball.ybounce()
                bricks[i].reset() # to remove the brick
                bricks.pop(i) # pop from the dictionary
                break # to exit for loop, otherwise gives an error that dictionary changed during iteration

    # If there are no more bricks left stop the game
    if len(bricks) == 0:
        game_is_on = False
        sketch.clear()
        sketch.write("You won! You final score: {}".format(score), align="center", font=("Courier", 24, "normal"))
    elif lives == 0:
        game_is_on = False
        sketch.clear()
        sketch.write("You lost :( You final score: {}".format(score), align="center", font=("Courier", 24, "normal"))
    my_ball.move()

screen.exitonclick()