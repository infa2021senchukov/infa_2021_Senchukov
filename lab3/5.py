from random import randint
import turtle
import math as m
turtle.tracer(10,1)
number_of_turtles = 50
steps_of_time_number = 1000

pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.turtlesize (0.5, 0.5)
    unit.speed(50)
    unit.goto(randint(-450, 450), randint(-390, 390))
for j in range(number_of_turtles):
    pool[j].right(randint(0, 360))
v=[0]*number_of_turtles
for i in range(number_of_turtles):
    v[i]=randint(1, 5)
for i in range(steps_of_time_number):
    for j in range(number_of_turtles):
        if abs(pool[j].position()[0])>445:
            pool[j].left(2 * (90-pool[j].heading()))
        if abs(pool[j].position()[1])>394:
            pool[j].right(2 *pool[j].heading())
        pool[j].forward(v[j])
            
        

