from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.draw_right()
        self.draw_left()

    def increase_right_score(self):
        self.clear()
        self.r_score += 1
        self.draw_right()
        self.draw_left()


    def increase_left_score(self):
        self.clear()
        self.l_score += 1
        self.draw_right()
        self.draw_left()


    def draw_right(self):
        self.goto(180, 200)
        self.write(self.r_score, align="center", font=("Corier", 80, "normal"))

    def draw_left(self):
        self.goto(-180, 200)
        self.write(self.l_score, align="center", font=("Corier", 80, "normal"))
