from paddle import Paddle
from turtle import Screen
from ball import Ball

#Setting up the screen size and colourr
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pyong")
game_is_on = True

screen.tracer(0)

paddle_left = Paddle((-350, 0))
paddle_right = Paddle((350, 0))
ball = Ball()





while game_is_on:
    screen.update()
    screen.listen()
    screen.onkey(paddle_right.paddle_up, "Up")
    screen.onkey(paddle_right.paddle_down, "Down")
    screen.onkey(paddle_left.paddle_up, "w")
    screen.onkey(paddle_left.paddle_down, "s")

























screen.exitonclick()