import turtle
turtle.Screen()

turtle.Screen().bgcolor("blue")

turtle.Screen().title("my first turtle")


polygon = turtle.Turtle()

polygon.pensize(90)

num_sude = 6

len_side = 70

angle = 360.0/num_sude

for i in range(num_sude):
    polygon.forward(len_side)
    polygon.right(angle)

turtle.done()