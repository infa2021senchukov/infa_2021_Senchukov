import turtle
turtle.shape('turtle')
def C(a):
    if a==0:    
        for i in range (0,360,1):
            turtle.left(1)
            turtle.forward(1)
    if a==1:
        for i in range (0,360,1):
            turtle.right(1)
            turtle.forward(1)
for j in range (3):
    for i in range (0,2,1):
        C(i)
    turtle.left(60)
turtle.done()
