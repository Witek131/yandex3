def f (x, p):
    if x<=35:
        return p%2 == 0
    if p==0:
        return 0
    h= [f(x-2, p-1), f(x-4, p-1),f(x//2+x%2, p-1)]
    return any(h) if p%2!=0 else all(h)
print([i for i in range(200,36,-1) if f(i,2)])
print([i for i in range(200,36,-1) if f(i,3) and not f(i, 1)])
print([i for i in range(200,36,-1) if f(i,4) and not f(i, 2)])
