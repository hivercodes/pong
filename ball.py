from turtle import Turtle
import time

class Ball(Turtle):

    def __init__(self):
        super(Ball, self).__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.setheading(45)

