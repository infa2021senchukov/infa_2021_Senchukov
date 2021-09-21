import turtle
turtle.shape('turtle')
for j in range (0,10,1):
        for i in range (0,4,1):
            turtle.left(90)
            turtle.forward(10+20*j)
        turtle.penup()
        turtle.forward(10)
        turtle.right(90)
        turtle.forward(10)
        turtle.left(90)
        turtle.pendown()
turtle.done()
