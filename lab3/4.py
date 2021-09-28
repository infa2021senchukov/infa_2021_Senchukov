import turtle as t
t.shape ('circle')
t.turtlesize (0.1, 0.1)
g = 9.81
dt=0.1
vx = 45
vy = 100
x, y = -400, 1
t.goto (400, 0)
t.goto (-400, 0)
for i in range (1000):
    t.goto(x,y)
    x=x+vx*dt
    y=y+vy*dt
    vy=vy-g*dt-0.0003*vy**2
    vx=vx-0.0003*vx**2
    if y<3.5:
        vy=-0.8*vy
        if abs(vy)<9:
            t.done()
        

