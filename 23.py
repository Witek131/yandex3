def f(x,y):
    if x==y:
        return 1
    elif x>y or x==35:
        return 0
    return f(x+1,y) + f(x+2, y) + f(x+4, y)

print(f(24, 33)*f(33,42))
меня не слышно
я тебя слышу

