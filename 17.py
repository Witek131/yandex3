f=list(map(int, open('17.txt').read().split()))
r =max([x for x in f if abs(x)%100 == 42 and 1000<=abs(x)<=9999])
k=0
e=[]
for a in zip(f, f[1:], f[2:]):
    s = [x for x in a if abs(x) % 100 == 42 and 1000 <= abs(x) <= 9999]
    # print(s, a)
    if len(s)>=2 and sum(a) > r:
        k+=1
        e.append(sum(a))
print(k, max(e))