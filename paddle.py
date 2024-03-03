from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.setposition(position)

    def up(self):
        """Make the paddle move up """
        if self.ycor() < 250:
            new_y = self.ycor()+20
            self.goto(self.xcor(),new_y)

    def down(self):
        """Make the paddle move down """
        if self.ycor() > -230:
            new_y = self.ycor() - 20
            self.goto(self.xcor(),new_y)

