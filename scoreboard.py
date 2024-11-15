from turtle import Turtle
import os

ALIGNMENT = "center"
FONT = ('Arial', 17, 'normal')

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.file_path = os.path.join(os.path.dirname(__file__), "data.txt")
        with open(self.file_path) as data:
            self.high_score = int(data.read())
        self.goto(0, 270)
        self.color('white')
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score : {self.score}       High score : {self.high_score}', align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(self.file_path, mode='w') as data:
                data.write(f'{self.high_score}')
        self.score = 0
        self.update_scoreboard()
        
    def score_added(self):
        self.score += 1
        self.update_scoreboard()
