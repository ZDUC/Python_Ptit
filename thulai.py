import math
def check(c):
    d=0
    while c>0:
        d=d+c%10
        c=int(c/10)
    return d
def snt(d):
    if d<2: return 0
    so=int(math.sqrt(d))+1
    for i in range(2,so):
        if d%i==0: return 0
    return 1
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    c=math.gcd(a,b)
    ds=check(c)
    if snt(ds)==1:
        print("YES")
    else :
        print("NO")