from functools import *
@lru_cache(maxsize=None)
def f(n):
    if n==41:
        return 1
    elif n>41 and n%2==0:
        return f(n-1) -n
    elif n>41 and n%2==1:
        return n*f(n-2)
for i in range(10000):
    f(i)
print(f(9094)/f(9089))
s=[0]*10000
s[41] =1
for i in range(42,10000):
    if i%2:
        s[i] = i*s[i-2]
    else:
        s[i]=s[i-1]-i
print(s[9094]/s[9089])