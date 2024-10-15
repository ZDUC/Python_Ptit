import math
def check(s):
    for i in range(2,int(math.sqrt(s))+1,1):
        if s%i==0 : return 0
    return 1
t=int(input())
for i in range(t):
    s=input()
    l=len(s)
    so=0
    for j in range(l):
        k=int(s[j])
        so=so+k
    if check(so)==1: print("YES")
    else : print("NO")