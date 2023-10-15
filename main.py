import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("cross the road")
screen.setup(width=600, height=600)
screen.tracer(0)
turtle = Player()
car = CarManager()
score=Scoreboard()
score.updates()

screen.listen()
screen.onkey(turtle.moves, "w")
screen.onkey(turtle.move_back,"s")
screen.onkey(turtle.leftturn,"a")
screen.onkey(turtle.rightturn,"d")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.mycar()
    car.car_moves()

    for cars in car.all_cars:
        if cars.distance(turtle) <= 20:
            game_is_on = False
            score.gameover()

    if turtle.finished():
        turtle.levelUPs()
        car.next_level()
        score.score()


screen.exitonclick()
