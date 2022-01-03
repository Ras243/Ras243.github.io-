import turtle

turtle.bgcolor("black")
turtle.pensize(3)
turtle.speed(0)

for x in range(12):
    for colours in ("red","blue","cyan","green","yellow","white"):
        turtle.color(colours)
        turtle.left(12)
        for i in range(4):
            turtle.forward(200)
            turtle.left(90)