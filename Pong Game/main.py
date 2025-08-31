from turtle import Screen
from paddle import Paddle
from ball import Ball
from scorebrd import Scoreboard
import time

screen= Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong Game")
screen.tracer(0)

r_side = Paddle((350,0))
l_side = Paddle((-350,0))
ball = Ball()
scorebrd = Scoreboard()

screen.listen()
screen.onkey(r_side.go_up,"Up")
screen.onkey(r_side.go_down,"Down")
screen.onkey(l_side.go_up,"w")
screen.onkey(l_side.go_down,"s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_side) < 50 and ball.xcor() > 320 or ball.distance(l_side) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_pos()
        scorebrd.l_point()

    if ball.xcor() < -380:
        ball.reset_pos()
        scorebrd.r_point()

screen.exitonclick()