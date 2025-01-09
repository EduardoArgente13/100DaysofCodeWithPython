import turtle as t
import random
#import colorgram

timmy = t.Turtle()
screen = t.Screen()
t.colormode(255)
directions = [0, 90, 180, 270]

timmy.shape("turtle")
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_color =  (r, g, b)
    return random_color

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

color_list = [(2, 13, 31), (52, 25, 17), (218, 128, 106), (11, 105, 159), (241, 213, 70), (149, 84, 40), (214, 87, 64), (156, 7, 24), (164, 162, 32), (156, 63, 102), (11, 62, 31), (206, 74, 104), (12, 96, 57), (93, 6, 21), (174, 135, 162), (1, 63, 145), (9, 173, 215), (157, 32, 22), (5, 212, 206), (10, 139, 86), (146, 226, 215), (121, 193, 149), (101, 219, 229), (222, 177, 213), (123, 171, 191), (80, 135, 179)]

# Drawing a square

# def square():
#     for _ in range(4):
#         timmy.forward(100)
#         timmy.left(90)
    
# square()


# Drawing a dashed line

# def dashed_line():
#     for _ in range(4):
#         timmy.left(90)
#         for _ in range(10):
#             timmy.forward(10)
#             timmy.penup()
#             timmy.forward(10)
#             timmy.pendown()
        
# dashed_line()


# Drawing a Different Shapes

# def draw_shapes(sides):
#     angle = 360 / sides
#     for _ in range(sides):
#         timmy.forward(100)
#         timmy.left(angle)

# for sides in range(3, 11):
#     timmy.color(random_color())
#     draw_shapes(sides)


#Drawing a random walk

# def random_walk():
#     timmy.pensize(10)
#     timmy.speed("fastest")
#     for _ in range(100):
#         timmy.color(random_color())
#         timmy.forward(30)
#         timmy.setheading(random.choice(directions))
    
# random_walk()

# def draw_circle(circle_heading):
#     circle_range = int(360 / circle_heading)
#     for _ in range(circle_range):
#         timmy.speed("fastest")
#         timmy.color(random_color())
#         timmy.circle(100)
#         current_heading = timmy.heading()
#         timmy.setheading(current_heading + circle_heading)
#         timmy.color(random_color())
#         timmy.circle(100)

# draw_circle(30)

# Hirst Painting

def hirst_painting():
    timmy.penup()
    timmy.speed("fastest")
    timmy.setheading(225)
    timmy.forward(300)
    timmy.setheading(0)
    number_of_dots = 100
    for dot_count in range(1, number_of_dots + 1):
        timmy.dot(20, random.choice(color_list))
        timmy.forward(50)
        if dot_count % 10 == 0:
            timmy.setheading(90)
            timmy.forward(50)
            timmy.setheading(180)
            timmy.forward(500)
            timmy.setheading(0)

hirst_painting()
screen.exitonclick()