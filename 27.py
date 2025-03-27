from math import *
from turtle import *
from random import *
def f1(n):
    m = 1000000
    for w in n:
        s=0
        for j in n:
            s+=dist(w,j)
        if m>s:
            m = s
            x= w[0]
            y= w[1]
    return x,y
f=open('27_A.txt').read().split('\n')
p = []
for line in f:
    x,y = [float(i) for i in line.split()]
    p.append((x,y))
clast = []
while p:
    s = [p.pop(0)]
    for i in s:
        sos = [p1 for p1 in p if dist(i, p1)<1.5]
        s.extend(sos)
        for d in sos: p.remove(d)
    clast.append(s)
x=0;y=0
tracer(0)
up()
screensize(2000,2000)
for i in clast:
    col = (random(),random(),random())
    for x, y in i:
            goto(x,y)
            dot(3, col)


for i in clast:
    print(f1(i))
    x += f1(i)[0]
    y += f1(i)[1]
update()
done()
print(x, y)
print((x/len(clast))*10000,(y/len(clast))*10000)