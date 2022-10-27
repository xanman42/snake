from turtle import Turtle

FONT = ('courier', 20, 'bold')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data:
            self.highscore = int(data.read())
        self.color('white')
        self.penup()
        self.ht()
        self.sety(270)
        self.write(f"Score : {self.score} Highscore : {self.highscore}", False, "center", FONT)

    def newscore(self):
        self.clear()
        self.write(f"Score : {self.score} Highscore : {self.highscore}", False, "center", FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.newscore()
        with open('data.txt', mode='w') as data:
            data.write(str(self.highscore))
