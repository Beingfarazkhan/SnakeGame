from turtle import Turtle
ALIGHNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore_data.txt", mode="r") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 310)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE : {self.score} | HIGHSCORE : {self.highscore}", align=ALIGHNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore :
            self.highscore = self.score
            with open("highscore_data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(" GAME OVER ", align=ALIGHNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()



