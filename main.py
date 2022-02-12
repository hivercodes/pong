from paddle import Paddle
from turtle import Screen
from ball import Ball
from scoreboard import Scoreboard
import time

#Setting up the screen size and colourr
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pyong")
game_is_on = True
scoreboard = Scoreboard()


#stops screen auto update
screen.tracer(0)


#creates paddles and balls
paddle_left = Paddle((-350, 0))
paddle_right = Paddle((350, 0))
ball = Ball()

#add listeners for keypresses
screen.listen()
screen.onkey(paddle_right.paddle_up, "Up")
screen.onkey(paddle_right.paddle_down, "Down")
screen.onkey(paddle_left.paddle_up, "w")
screen.onkey(paddle_left.paddle_down, "s")



#main loop
while game_is_on:
    screen.update()
    time.sleep(ball.movespeed)
    ball.move()
    #checks collision with walls
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()
    #checks collsision with right paddle
    if ball.distance(paddle_right) < 40 and ball.xcor() > 340 or ball.distance(paddle_left) < 40 and ball.xcor() < 340:
        ball.ball_return()



    #check if right misses
    if ball.xcor() > 380:
        sleep_time = 0.1
        ball.reset()
        scoreboard.increase_left_score()

    if ball.xcor() < -380:
        sleep_time = 0.1
        ball.reset()
        scoreboard.increase_right_score()

























screen.exitonclick()