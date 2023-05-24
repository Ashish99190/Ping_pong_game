from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.update_score()



    def update_score(self):
        self.goto(-100, 260)
        self.write(arg=f"{self.l_score}", align='center', font=('courier', 30, 'normal'))
        self.goto(100, 260)
        self.write(arg=f"{self.r_score}", align='center', font=('courier', 30, 'normal'))

    def l_point(self):
        self.l_score += 1
        self.update_score()


    def r_point(self):
        self.r_score += 1
        self.update_score()


