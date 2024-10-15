for i in range(int(input())):
    x=1
    ds=0
    n,p=map(int,input().split())
    while n/(p**x)>1:
        ds=ds+int(n/(p**x))
        x=x+1
    print(ds)