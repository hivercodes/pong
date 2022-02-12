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


    def move(self):

        new_x = self.xcor() + 5
        if self.ycor() == 280:
            self.going_up = False
        if self.ycor() == -280:
            self.going_up = True

        if self.going_up:
            new_y = self.ycor() + 5
        else:
            new_y = self.ycor() - 5
            


        self.goto(new_x, new_y)
