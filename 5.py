s = f'{5:b}'
s = s + str(s.count('1') % 2)
s = s + str(s.count('1') % 2)
print(int(s,2))
d=[]
for i in range(2, 1000):
    s = f'{i:b}'
    s = s + str(s.count('1') % 2)
    s = s + str(s.count('1') % 2)
    r =int(s,2)
    if r>198:
        d.append(r)
print(min(d))