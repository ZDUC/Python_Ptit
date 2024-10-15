import math
def check(s):
    l=len(s)
    if l<2: return 0
    for i in range(int(l/2)):
        if s[i]!=s[l-1-i]: return 0
    return 1
t=int(input())
for i in range(t):
    s=input()
    l=len(s)
    so=0
    for j in range(l):
        k=int(s[j])
        so=so+k
    q=str(so)
    if check(q)==1: print("YES")
    else : print("NO")