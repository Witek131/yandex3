f=list(map(int, open('17.txt').read().split()))
r =max([x for x in f if x%100 == 42])
k=0
e=[]
for a in zip(f, f[1:], f[2:]):
    s=0
    for j in a:
        if j%100 ==42:
            s+=1
    if s>=2 and sum(a) > r:
        k+=1
        e.append(sum(a))
print(k, max(e))