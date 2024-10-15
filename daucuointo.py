import math
def kt(n):
    if n<2: return 0
    for i in range(2,int(math.sqrt(n)),1):
        if n%i==0: return 0
    return 1
t=int(input())
for i in range(t):
    s=input()
    dau=int(s[:3])
    cuoi=int(s[len(s)-3::])
    if kt(dau)==1 and kt(cuoi)==1: print("YES")
    else : print("NO")