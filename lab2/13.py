import turtle
turtle.shape('turtle')
def C(a,b,c):
    if a==0:    
        for i in range (0,c,1):
            turtle.left(1)
            turtle.forward(b)
    if a==1:
        for i in range (0,c,1):
            turtle.right(1)
            turtle.forward(b)
turtle.penup()
turtle.goto(0,-75)
turtle.pendown()
turtle.color('black','yellow')
turtle.begin_fill()
C(0,2.5,360)
turtle.end_fill()
turtle.color('black','blue')
turtle.penup()
turtle.left(90)
turtle.goto(-50,145)
turtle.pendown()
turtle.begin_fill()
C(0,0.3,360)
turtle.end_fill()
turtle.penup()
turtle.goto(75,145)
turtle.pendown()
turtle.begin_fill()
C(0,0.3,360)
turtle.end_fill()
turtle.color('black')
turtle.penup()
turtle.goto(0,145)
turtle.pendown()
turtle.penup()
turtle.goto(0,100)
turtle.pendown()
turtle.pensize(10)
turtle.left(180)
turtle.forward(30)
turtle.penup()
turtle.goto(-60,20)
turtle.pendown()
turtle.color('red')
C(0,1.05,180)
