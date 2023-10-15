from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)


    def moves(self):
        self.fd(MOVE_DISTANCE)


    def move_back(self):
        self.backward(MOVE_DISTANCE)

    def leftturn(self):
        self.left(90)
        self.fd(MOVE_DISTANCE)
        self.right(90)


    def rightturn(self):
        self.right(90)
        self.fd(MOVE_DISTANCE)
        self.left(90)




    def levelUPs(self):
        self.goto(STARTING_POSITION)

    def finished(self):
        if self.ycor() > 280:
            return True
        else:
            return False
