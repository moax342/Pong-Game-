from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.goto(0, 0)
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        # determent the speed of the ball
        self.move_speed=0.1

    def ball_moving(self):
        """make the ball move when its first created """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """make the ball bounce from the Y axes"""
        self.y_move *= -1

    def bounce_x(self):
        """make the ball bounce from the X axes"""
        self.x_move *= -1

    def reset_position(self):
        """reset the position of the ball when its hits the wall """
        self.goto(0,0)
        self.bounce_x()
