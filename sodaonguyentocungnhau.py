def ucln(a,b):
    while a*b!=0:
        if a>b:
            a=a%b
        else:
            b=b%a
    return a+b
t=int(input())
for i in range(t):
    a=input()
    st=int(a)
    b=""
    b=a[::-1]
    sd=int(b)
    if ucln(st,sd)==1:
        print("YES")
    else :
        print("NO")