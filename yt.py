import math
t=int(input())
mod=1000
for i in range(t):
    n=int(input())
    ds=int((3+math.sqrt(5))**n)
    for j in range(10):
        if ds>=1000: 
            ds=ds%mod
            j=j-1
        else : break
    print(ds)
    