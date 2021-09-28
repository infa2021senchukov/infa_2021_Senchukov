import turtle as t
from ast import literal_eval

inp = open('3.txt', 'r')
a = inp.readlines()
inp.close()
t.shape('turtle')
t.color('blue')
t.penup()
t.goto(-300,0)
t.pendown
s=[0]*10
for i in range (10):
    s[i]=literal_eval(a[i])
b=int(input())
d=0
e=b
while b>10:
    b=b//10
    d=d+1
c=[0]*(d+1)
for i in range (d+1):
    c[i]=e%10
    e=e//10
c.reverse()
print(c)
for i in c:
    for j in range (len(s[i])):
        if s[i][j][1]==0:
            t.penup()
            t.right(s[i][j][0])
            t.forward(s[i][j][2])
        else:
            t.pendown()
            t.right(s[i][j][0])
            t.forward(s[i][j][2])
t.done()
