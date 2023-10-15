from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-220,260)
        self.level=1


    def score(self):
        self.level+=1
        self.updates()


    def updates(self):
        self.clear()
        self.write(f"level: {self.level}",align="center",font=FONT)


    def gameover(self):
        self.goto(0,0)
        self.write("gameover",align="center",font=FONT)

