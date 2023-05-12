from turtle import Turtle, write
ALIGNMENT = 'center'
FONT = ('Arial', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as file:
            self.highscore = int(file.read())
        self.color('white')
        self.penup()
        self.highscore = 0
        self.goto(0, 270)
        self.write(
            f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def point(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.point()
