from itertools import product
k=0
for i in product('артём', repeat=5):
    s = ''.join(i)
    if len(set(s))==5 and ((s[0] in 'аё' and s[-1] not in  'аё') or (s[-1] in 'аё' and s[0] not in  'аё')):
        print(s)
        k+=1
print(k)