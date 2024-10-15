while 1:
    n=int(input())
    if n==0: break
    s=input()
    min=int(s)
    max=int(s)
    for i in range(n-1):
        so=input()
        if int(so)<min: min=int(so)
        if int(so)>max: max=int(so)
    if min==max: 
        print("BANG NHAU")
        continue
    print(min, end=" ")
    print(max)
    print()