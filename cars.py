from turtle import Turtle
import random

CARS = []
COLORS = ["red", "blue", "green", "yellow", "orange"]
POSITION_X = random.randint(1, 500)
POSITION_Y = random.randint(1, 300)
STARTING_MOVE = 5
MOVE_INCREMENT = 10



class Cars:
    def __init__(self):
        self.all_cars = []
        self.car_speed = 0.1

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_cars = Turtle("square")
            new_cars.shapesize(stretch_wid=1, stretch_len=2)
            new_cars.penup()
            new_cars.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_cars.goto(500, random_y)
            self.all_cars.append(new_cars)

    def move_cars(self):
        for cars in self.all_cars:
            cars.backward(STARTING_MOVE)

    def increase_car_speed(self):
        self.car_speed *= 0.9
