from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.setheading(90)
        self.turtlesize(stretch_wid=0.7, stretch_len=4)
        self.goto(position)

    def up(self):
        self.forward(40)

    def down(self):
        self.backward(40)

    # def up_l(self):
    #     self.forward(40)
    #
    # def down_l(self):
    #     self.backward(40)







