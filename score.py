from turtle import  Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0,y=325)
        self.hideturtle()
        self.write(arg=f"Score:{self.score}",align="center",font=("Roboto", 15, "bold"))

    def inc_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score:{self.score}", align="center", font=("Roboto", 15, "bold"))

    def game_over(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=0)
        self.write(arg=f"Game Over", align="center", font=("Roboto", 25, "bold"))