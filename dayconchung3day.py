for j in range(int(input())):
    n,m,k=map(int,input().split())
    a=[int(i) for i in input().split()]
    b=[int(i) for i in input().split()]
    c=[int(i) for i in input().split()]
    check,m1,m2,m3=0,0,0,0
    while m1<n and m2<m and m3<k:
        if a[m1]==b[m2]==c[m3]:
            check=1
            print(a[m1],end=" ")
            m1,m2,m3=m1+1,m2+1,m3+1
        elif a[m1]<b[m2]: m1=m1+1
        elif b[m2]<c[m3]: m2=m2+1
        else: m3=m3+1
    if check==0: print("NO")
    print()
