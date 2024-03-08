from turtle import Screen
from cars import Cars
from player_car import PlayerTurtle
import time
from score import ScoreBoard
cars = Cars()
screen = Screen()
score = ScoreBoard()
screen.tracer(0)
user_turtle = PlayerTurtle()
screen.setup(1000, 600)

game_is_on = True
screen.listen()
screen.onkeypress(user_turtle.move_up, "Up")
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move_cars()

    if user_turtle.ycor() > 290:
        score.update_level()
        user_turtle.restart_turtle()
        cars.increase_car_speed()

    for car in cars.all_cars:
        if car.distance(user_turtle) < 25:
            game_is_on = False

screen.exitonclick()
