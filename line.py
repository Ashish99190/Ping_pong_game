from turtle import Turtle


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 250)
        self.setheading(270)
        self.draw()

    def draw(self):
        for _ in range(int(500/20)):
            self.speed("fastest")
            self.pensize(8)
            self.color("white")
            self.hideturtle()
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)



