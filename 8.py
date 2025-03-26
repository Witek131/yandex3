from itertools import product
k=0
for i in product('артем', repeat=5):
    s = ''.join(i)
    if len(set(s))==5 and s[0] not in 'ае' and s[-1] not in 'ае':
        print(s)
        k+=1
print(k)