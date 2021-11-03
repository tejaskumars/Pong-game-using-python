from turtle import Screen
from turtle import Turtle
from Paddles import Create_Paddle
from ball import Ball
from score import Score_board
import time
s = Screen()
s.bgcolor("black")
s.screensize(800,600)
s.title("Bong")
s.tracer(0)

#drawing center line 
line = Turtle()
line.color("white")
line.hideturtle()
line.penup()
line.goto(0,-300)
line.left(90)
line.pensize(10)
line.speed("fastest")
while(line.ycor() < 320 ):
    line.pendown()
    line.forward(20)
    line.penup()
    line.forward(20)


paddle_left = Create_Paddle(-350,-280)
paddle_right = Create_Paddle(350,-280)
bottom_paddle = Create_Paddle(0,-300)
bottom_paddle.left(90)
ball = Ball()
score = Score_board()

s.listen()

s.onkey(paddle_left.move_up,"w")
s.onkey(paddle_left.move_down,"s")
s.onkey(paddle_right.move_up,"Up")
s.onkey(paddle_right.move_down,"Down")

game_on = True

while(game_on):
    time.sleep(ball.move_speed)
    s.update()
    ball.move()


    #detect collision with upper and lower wall
    if(ball.ycor()> 280 or ball.ycor() < -280):
        ball.bounce_y()

    if(paddle_right.distance(ball) < 50 and ball.xcor() > 320):
        ball.bounce_x()

    if(paddle_left.distance(ball) < 50 and ball.xcor() <  -320):
        ball.bounce_x()
    
    #detect side walls 
    if (ball.xcor() > 370):
        score.l_point()
        ball.reset()
    if (ball.xcor() < -370):
        score.r_point()
        ball.reset()

    if(score.l_score == 3 or score.r_score == 3):
        score.game_over()
        game_on = False
        ball.goto(0,0)

        
    









s.exitonclick()















