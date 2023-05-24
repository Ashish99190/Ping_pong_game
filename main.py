from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time
screen = Screen()
score = Score()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_r = Paddle((380, 0))
paddle_l = Paddle((-380, 0))
ball = Ball()

screen.listen()
screen.onkey(paddle_r.up, "Up")
screen.onkey(paddle_r.down, "Down")
screen.onkey(paddle_l.up, "w")
screen.onkey(paddle_l.down, "s")

game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if (ball.distance(paddle_r) < 50 and ball.xcor() > 350) or (ball.distance(paddle_l) < 50 and ball.xcor() < -350):
        ball.paddle_bounce()

    if ball.xcor() > 400:
        ball.reset_pos()
        score.clear()
        score.l_point()

    if ball.xcor() < -400:
        ball.reset_pos()
        score.clear()
        score.r_point()






























screen.exitonclick()