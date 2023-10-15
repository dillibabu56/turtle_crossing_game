from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
X=320
game=True


class CarManager():
    def __init__(self):
        self.all_cars=[]
        self.MOVE_SPEED = STARTING_MOVE_DISTANCE
    def mycar(self):
        random_chance=random.randint(1,6)
        if random_chance==1:
            car=Turtle()
            car.color(random.choice(COLORS))
            car.penup()
            car.setheading(180)
            car.shape("square")
            car.goto(X, random.randint(-250, 250))
            car.shapesize(stretch_wid=1, stretch_len=2)
            self.all_cars.append(car)

    def next_level(self):
        self.MOVE_SPEED += MOVE_INCREMENT

    def car_moves(self):
        for i in self.all_cars:
            i.forward(self.MOVE_SPEED)





