from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-200, 260)
        self.write(f"Left: {self.l_score}", align="left", font=("Courier", 24, "normal"))
        self.goto(200, 260)
        self.write(f"Right: {self.r_score}", align="right", font=("Courier", 24, "normal"))

    def increase_score_l(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def increase_score_r(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))