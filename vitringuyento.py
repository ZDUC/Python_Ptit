import math
def nto(j):
    if j<2: return 0
    for i in range(2,int(math.sqrt(j))+1):
        if j%i==0: return 0
    return 1
t=int(input())
for i in range(t):
    s=input()
    check=0
    l=len(s)
    for j in range(l):
        if nto(j)==1:
            if s[j]=='2' or s[j]=='3' or s[j]=='5' or s[j]=='7':
                check=check+1
        if nto(j)==0:
            if s[j]!='2' and s[j]!='3' and s[j]!='5' and s[j]!='7':
                check=check+1
    if check==len(s):
        print("YES")
    else :
        print("NO")