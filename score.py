from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("aqua")
        self.goto(0,270)
        with open("high.txt") as file:
            self.high_score = int(file.read())
        self.current_score = 0
        self.write(f"score: {self.current_score}, High score: {self.high_score}", align="center", font=('Arial', 22, 'normal'))
        self.hideturtle()

    # def gameover(self):
    #     self.goto(0,0)
    #     self.write(f"GAMEOVER", align="center", font=('Arial', 30, 'normal'))

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("high.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.current_score = 0
        self.update_score()

    def increse_score(self):
        self.current_score += 1
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f"score: {self.current_score}, High score: {self.high_score}", align="center", font=('Arial', 22, 'normal'))
