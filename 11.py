import turtle
turtle.shape('turtle')
turtle.left(90)
def C(a,b):
    if a==0:    
        for i in range (0,360,1):
            turtle.left(1)
            turtle.forward(b)
    if a==1:
        for i in range (0,360,1):
            turtle.right(1)
            turtle.forward(b)
for j in range (10):
    for i in range (0,2,1):
        C(i,j*0.15+0.8)
turtle.done()
