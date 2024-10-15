n=int(input())
a=[]
a=list(map(int,input().split()))
a.sort()
ds1=a[n-1]*a[n-2]*a[n-3]
ds2=a[n-1]*a[n-2]
ds3=a[0]*a[1]
ds4=a[0]*a[1]*a[n-1]
max=max(ds1,ds2,ds3,ds4)
print(max)

    
