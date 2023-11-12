from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
from winner import Winner

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0), "blue")
l_paddle = Paddle((-350, 0), "red")
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #   Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #   Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #   Detect r_paddle miss
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()
        game_is_on = scoreboard.winner()

    #   Detect l_paddle miss
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()
        game_is_on = scoreboard.winner()

if game_is_on == False:
    screen.clear()
    screen.bgcolor("black")
    Winner(scoreboard)


screen.exitonclick()