import turtle
turtle.shape('turtle')
def C(a,b):
    if a==0:    
        for i in range (0,180,1):
            turtle.left(1)
            turtle.forward(b)
    if a==1:
        for i in range (0,180,1):
            turtle.right(1)
            turtle.forward(b)
turtle.left(90)
turtle.penup()
turtle.goto(-250,0)
turtle.pendown()
for i in range (4):
    C(1,1)
    C(1,0.1)
C(1,1)
