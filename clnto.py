import math
def check(s):
    n=len(s)
    tcs=0
    if n < 2 : return 0
    for i in range(0,n,2):
        k= int(s[i])
        l= int(s[i+1])
        if k%2!=0: return 0
        if l%2==0: return 0
        tcs=tcs+l+k
    for i in range(2, int(math.sqrt(tcs)) + 1) :
        if tcs % i == 0 : return 0
    return 1
t=int(input())
for i in range(t):
    s=input()
    if check(s)==1 : print("YES")
    else : print("NO")        