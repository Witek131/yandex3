from math import *
from turtle import *
from random import *


def f1(n):
    m = 1000000
    print(n)
    for w in n:
        s = 0
        for j in n:
            s += dist(w, j)
        if m > s:
            m = s
            x = w[0]
            y = w[1]
    return x, y


f = open('27_B.txt').read().split('\n')
p = []
for line in f:
    x, y = [float(i) for i in line.split()]
    x1 = y*cos(x*(pi/180))
    y1 = y*sin(x*(pi/180))
    # print(x,y, x1,y1)
    p.append((x1, y1))
clast = []
while p:
    s = [p.pop(0)]
    for i in s:
        sos = [p1 for p1 in p if dist(i, p1) < 10]
        s.extend(sos)
        for d in sos: p.remove(d)
    clast.append(s)
x = 0;
y = 0
tracer(0)
up()
screensize(2000, 2000)
for i in clast:
    col = (random(), random(), random())
    for x, y in i:
        goto(x*2, y*2)
        dot(3, col)
x3,y3=0,0
for i in clast:
    mas = f1(i)
    x3 += mas[0]
    y3 += mas[1]
update()
done()
print(x3, y3,1)
print((x3 / len(clast)) * 10000, (y3 / len(clast)) * 10000)
