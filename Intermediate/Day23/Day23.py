import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
carManager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carManager.create_car()
    carManager.move_cars()

    # Check for collision with car
    for car in carManager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
    
    # Check if player has reached the top edge
    if player.ycor() > 280:  # Assuming the top edge is at y=280
        player.goto(0, -280)  # Reset player position
        scoreboard.increase_score()  # Increase the score
        carManager.level_up()

screen.exitonclick()