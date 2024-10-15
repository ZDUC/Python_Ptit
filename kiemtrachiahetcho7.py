t = int(input())
for i in range(t) :
    n = int(input())
    m=0
    while n % 7 != 0 :
        n += int(str(n)[::-1])
        m=m+1
        if m==1000 :break
    if m<1000 : print(n)