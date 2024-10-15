t=int(input())
for i in range(t):
    n=int(input())
    x,y,z=map(int, input().split())
    m=[999999]*(n+1)
    m[1]=x
    for i in range(2,n+1):
        if i%2==0:
            m[i]=min(m[i-1]+x,m[i//2]+z)
        else:
            m[i]=min(m[i-1]+x,m[i//2+1]+z+y)
    print(m[n])
    
            