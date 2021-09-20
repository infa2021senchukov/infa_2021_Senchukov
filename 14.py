import turtle
turtle.shape('turtle')
def S(n):
    if n%2==1:
        turtle.left(180)
        for i in range (n):
            turtle.forward(100)
            turtle.left(180-180/n)
    else:
        for i in range (n):
            turtle.forward(100)
            turtle.left(360/n)
            turtle.forward(100)
            turtle.left(180+360/n)
            
S(5)
turtle.penup()
turtle.goto(100,0)
turtle.pendown()
S(11)

