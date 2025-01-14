from turtle import Turtle, Screen
from Paddle import Paddle
from Ball import Ball
from Scoreboard import Scoreboard
import time

# Configuración inicial de la pantalla
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Configuración de jugadores
paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))

# Configuración de la pelota
ball = Ball()

# Configuración del marcador
scoreboard = Scoreboard()

# Configuración de controles
screen.listen()
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")



game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    scoreboard.update_scoreboard()
    ball.move()

    # Detectar colisión con la pared
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detectar colisión con las paletas
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detectar punto para el jugador derecho
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_score_l()

    # Detectar punto para el jugador izquierdo
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_score_r()

        
screen.exitonclick()