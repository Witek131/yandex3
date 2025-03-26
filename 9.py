f = open('9.csv').read().split('\n')
k=0
for i in f:
    s = [int(j) for j in i.split(';')]
    if len(set(s))==4 and (min(s)+max(s))/2 <=(sum(s)-(min(s)+max(s)))/2:
        k+=1
print(k)
