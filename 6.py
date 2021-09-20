import turtle
turtle.shape('turtle')
a=int(input())
for i in range (0,a,1):
        turtle.forward(50)
        turtle.left(180)
        turtle.forward(50)
        turtle.left(180)
        turtle.right(360/a)
turtle.done()
