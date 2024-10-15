
def transfer(num):
    s=str(num)
    ch=1
    for i in s: ch=ch*int(i)
    return ch
for i in range(int(input())):
    n=int(input())
    a=[int(j) for j in input().split()]
    for j in range(n-1):
        for k in range(j+1,n):
            if transfer(a[k])<transfer(a[j]): a[j],a[k]=a[k],a[j]
            if transfer(a[k])==transfer(a[j]):
                if a[k]<a[j]: a[j],a[k]=a[k],a[j]
    for l in a: print(l,end=" ")
    print()