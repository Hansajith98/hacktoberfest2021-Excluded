ALIGNMENT="center"
FONT=("Cpurier",15,"normal")


from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        # self.high_score_string=''
        with open("high_score.txt", mode="r") as file:
            self.high_score_string=file.read()
        self.highscore=int(self.high_score_string)
        self.color("white")
        self.penup()
        self.goto(x=-10, y=325)
        self.score=0
        self.refresh_score()
        self.hideturtle()
        self.refresh_score()


    def refresh_score(self):
        self.write(arg=f"Score = {self.score}      High Score = {self.highscore}", font=FONT, align=ALIGNMENT)


    def game_over(self):
        # self.clear()
        self.goto(0, 0)
        self.penup()
        self.write(arg="GAME OVER", font=FONT, align=ALIGNMENT)


    def high_score_update(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.highscore))


    def update_score(self):
        self.score+=1
        self.high_score_update()
        self.clear()
        self.refresh_score()

