import turtle
import math as np
turtle.shape('turtle')
def N(i):
    turtle.left(90*(i+2)/i)
    for j in range (1,i+1,1):
        turtle.forward(2*(20*(i-3)+30)*np.sin(np.pi/i))
        turtle.left(360/i)
    turtle.right(90*(i+2)/i)
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()
for i in range (3,11,1):
    N(i)
turtle.done()
