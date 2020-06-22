import turtle
height = 10
width = 10
turtle.shape('turtle')
turtle.speed(1)
turtle.penup()

for y in range(height):
    for x in range(width):
        turtle.dot()
        turtle.forward(30)
    turtle.backward(30 * width)
    turtle.right(90)
    turtle.forward(30)
    turtle.left(90)
    
turtle.exitonclick()