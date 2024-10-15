for i in range(int(input())):
    d={}
    n=int(input())
    l=[int(j) for j in input().split()]
    for j in l:
        if j in d: d[j]+=1
        else: d[j]=1
    check=0
    for j in d:
        if d[j] > int(n/2): 
            print(j)
            check=1
            break
    if check==0: print("NO")