import turtle as turtle_module
import random
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('download.png', 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)


color_list = [(199, 175, 117), (125, 36, 24), (187, 158, 51), (170, 106, 56), (5, 57, 83), (200, 215, 205), (222, 222, 225), (108, 67, 85), (88, 142, 56), (110, 160, 175), (20, 122, 176), (76, 39, 48), (63, 153, 138),
              (9, 68, 47), (134, 41, 43), (183, 97, 80), (179, 201, 186), (208, 199, 128), (148, 173, 160), (174, 165, 169), (28, 78, 60), (97, 141, 153), (210, 184, 176), (22, 77, 95), (195, 189, 191), (139, 120, 124), (175, 197, 204)]

turtle_module.colormode(255)
tim = turtle_module.Turtle()

tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
