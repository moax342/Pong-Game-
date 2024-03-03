from turtle import Turtle

ALIGNMENT = "center"
FONT =("Courier", 24, "bold")

class ScoreBoard(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.score = 0
        self.color("white")
        self.goto(position)
        self.hideturtle()
        self.update_score_board()

    def update_score_board(self):
        """write the score to the board """
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def add_point(self):
        """add score to the variable score to be updated """
        self.score += 1
        self.clear()
        self.update_score_board()