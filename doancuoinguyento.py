import math
def kt(n):
    if n<2: return 0
    for i in range(2,int(math.sqrt(n)),1):
        if n%i==0: return 0
    return 1
t=int(input())
for i in range(t):
    s=input()
    so=int(s[len(s)-4::])
    if kt(so)==1: print("YES")
    else: print ("NO")