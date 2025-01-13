from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Crea los segmentos iniciales de la serpiente."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Añade un segmento a la serpiente en una posición específica."""
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def move(self):
        """Hace que la serpiente se mueva hacia adelante."""
        # Los segmentos siguen al primer segmento
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        # La cabeza se mueve hacia adelante
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        """Hace que la serpiente se mueva hacia arriba."""
        if self.head.heading() != DOWN:
            self.head.setheading(90)
    
    def down(self):
        """Hace que la serpiente se mueva hacia abajo."""
        if self.head.heading() != UP:
            self.head.setheading(270)
    
    def left(self): 
        """Hace que la serpiente se mueva hacia la izquierda."""
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
    
    def right(self):
        """Hace que la serpiente se mueva hacia la derecha."""
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def extend(self):
        """Añade un nuevo segmento a la serpiente."""
        self.add_segment(self.segments[-1].position())
