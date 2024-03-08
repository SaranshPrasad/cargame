from turtle import Turtle


class PlayerTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0, -280)
        self.new_y = 0
        self.left(90)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def restart_turtle(self):
        self.goto(0, -280)