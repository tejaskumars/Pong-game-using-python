from turtle import Turtle


class Create_Paddle(Turtle):

    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.hideturtle()
        self.moving = True
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(self.x,self.y)
        self.showturtle()

    def move_up(self):
        new_y = self.ycor()+50
        self.goto(self.xcor(),new_y)

    def move_down(self):
        new_y = self.ycor()-50
        self.goto(self.xcor(),new_y)

        