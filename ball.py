from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        # self.shapesize(stretch_wid=2,stretch_len=2)
        self.penup()
        self.goto(0,-280)
        self.x_move = 10
        self.Y_move = 10
        self.move_speed = 0.1


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.Y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.Y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0,-280)
        self.move_speed = 0.1
        self.bounce_x()
