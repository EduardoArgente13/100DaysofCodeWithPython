from turtle import Turtle, Screen
import random

def setup_screen():
    """Sets up the program screen."""
    screen = Screen()
    screen.setup(width=500, height=400)
    return screen

def get_user_bet(screen, colors):
    """Gets the user's bet and validates that it is an available color."""
    user_bet = screen.textinput(title="Make your bet", 
                                prompt=f"Which turtle will win the race? Choose from: {', '.join(colors)}")
    while user_bet not in colors:
        user_bet = screen.textinput(title="Invalid choice", 
                                    prompt=f"Please choose a valid color: {', '.join(colors)}")
    return user_bet

def create_turtles(colors):
    """Creates and positions the turtles at the starting line."""
    turtles = []
    for i, color in enumerate(colors):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(color)
        new_turtle.penup()
        new_turtle.goto(x=-230, y=-100 + (i * 40))
        turtles.append(new_turtle)
    return turtles

def start_race(turtles, user_bet):
    """Starts the race and determines the winner."""
    is_race_on = True
    while is_race_on:
        for turtle in turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")
                return
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)

# Main program
def main():
    screen = setup_screen()
    colors = ["red", "orange", "gold", "green", "blue", "purple"]
    user_bet = get_user_bet(screen, colors)
    turtles = create_turtles(colors)
    if user_bet:
        start_race(turtles, user_bet)
    screen.exitonclick()


main()




# def turn_right():
#     timmy.right(10)

# def turn_left():
#     timmy.left(10)

# def move_forward():
#     timmy.forward(10)

# def move_backward():
#     timmy.backward(10)

# def clear_screen():
#     timmy.clear()
#     timmy.penup()
#     timmy.home()
#     timmy.pendown()

# screen.listen()
# screen.onkey(key="d", fun=turn_right)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="c", fun=clear_screen)
