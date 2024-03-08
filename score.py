from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.goto(-490, 250)
        self.color("black")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level : {self.level}", align="left", font=("Courier", 20, "normal"))

    def update_level(self):
        self.level += 1
        self.update_score()
