import turtle

turtle.shape('turtle')
turtle.speed(5)

for side_length in range(100, 200, 10):
    for i in range(4):
        turtle.forward(side_length)
        turtle.left(120) 

turtle.exitonclick()