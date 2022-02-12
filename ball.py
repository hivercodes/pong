from turtle import Turtle
import time

class Ball(Turtle):

    def __init__(self):
        super(Ball, self).__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.setheading(45)
        self.going_up = True
        self.x_move = 10
        self.y_move = 10


    def move(self):

        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def bounce(self):
        self.y_move *= -1


    def ball_return(self):
        self.x_move *= -1