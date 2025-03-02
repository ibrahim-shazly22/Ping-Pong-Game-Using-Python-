from turtle import Turtle
FONT=("arial",8,"normal")
ALIGIN="center"
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score=0
        self.l_score=0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=self.l_score, align="center", font=(("arial", 80, "normal")))
        self.goto(100, 200)
        self.write(arg=self.r_score, align="center", font=(("arial", 80, "normal")))

    def left_score(self):
        self.l_score += 1
        self.update_scoreboard()


    def right_score(self):
        self.r_score+=1
        self.update_scoreboard()



