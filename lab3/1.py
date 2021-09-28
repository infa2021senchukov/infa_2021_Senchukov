import turtle as t
import random as r
t.shape('turtle')
t.color('red')
for i in range (100):
    t.forward(100*r.random())
    t.left(360*(r.random()-1))
t.done()
