from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen= Screen()
turtle=Turtle()
screen.screensize(800,600)
screen.bgcolor("black")
screen.title("                                                                                           #ONLINE AIR HOKEY GAME")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball =Ball()
score=Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"Left")
screen.onkey(l_paddle.go_down,"Right")

game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() >280 or ball.ycor()<-280:
        ball.bounce_y()

    if ball.distance(r_paddle)<50 and ball.xcor() > 340 or  ball.distance(l_paddle)<50 and ball.xcor() > -340:
        ball.bounce_x()

    if ball.xcor()> 380:
        ball.restart()
        score.l_point()

    if ball.xcor()< -380:
        ball.restart()
        score.r_point()

screen.exitonclick()
