n,m=map(int,input().split())
a=sorted(set(map(int,input().split())))
b=sorted(set(map(int,input().split())))
check=0
if len(a)!=len(b):
    print("NO")
    check=1
if check==0:
    for i in range(len(a)):
        if a[i]!=b[i]:
            print("NO")
            check=1
if check==0:
    print("YES")
