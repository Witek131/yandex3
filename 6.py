import turtle
from turtle import *
tracer(0)
# print(dir(turtle), help(turtle.back))
screensize(5000,5000)
k=10
for i in range(5):
    fd(35*k)
    rt(90)
    fd(24*k)
    rt(90)
up()
rt(90)
fd(7*k)
rt(90)
fd(5*k)
down()
for i in range(5):
    rt(90)
    fd(20 * k)
    rt(90)
    fd(36 * k)
up()
for x in range(-50,50):
    for y in range(-50, 50):
        goto(x*k,y*k)
        dot(3, 'red')
update()
done()
