from re import *
f=open('24.txt').read()
s=sub('SQRP', '8', f)
print(findall('P888888888888SQR',s) )

# for i in range(0,len(f)-4, 4):
#     print(f[i:i+4])
#     if f[i:i+4] == 'SQRP':
#         r+=4
    # else:
    #     if i!=0:
    #         if
    #
    #     r=0
