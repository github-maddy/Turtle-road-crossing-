import time
from turtle import Screen,Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
car = CarManager()
score = Scoreboard()

player = Player()

screen.listen()
screen.onkey(player.go_up,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.add_cars()
    car.move_cars()

    for i in car.all_cars:
        if i.distance(player)<20:
            game_is_on = False
            t=Turtle()
            t.hideturtle()
            t.penup()
            t.write(f"Game Over", align="center", font = ("Courier", 20, "normal"))


    if player.at_finish_line():
        player.goto_start()
        car.increse_speed()
        score.increase_level()



screen.exitonclick()