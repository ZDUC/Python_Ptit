import math
def check(n):
    if n < 2 : return 0
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0 : return 0
    return 1
t=int(input())
for i in range(t) :
    s=input()
    l=len(s)
    dnt=0
    if check(l)==0 :
        print("NO")
        continue
    for j in range(l):
        k=int(s[j])
        if check(k)==1 : dnt=dnt+1
    if dnt>(l-dnt) : print("YES")
    else : print("NO")