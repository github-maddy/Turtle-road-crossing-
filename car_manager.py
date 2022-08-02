import turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
from turtle import Turtle
import random

class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = 5

    def add_cars(self):
        random_int = random.randint(1,6)
        if random_int == 1:
            t = Turtle()
            t.shape("square")
            t.shapesize(stretch_wid=1, stretch_len=2)
            t.penup()
            t.color(random.choice(COLORS))
            random_y = random.randint(-250,250)
            t.goto(300,random_y)
            self.all_cars.append(t)

    def move_cars(self):
        for i in self.all_cars:
            i.backward(self.car_speed)

    def increse_speed(self):
        self.car_speed += MOVE_INCREMENT


