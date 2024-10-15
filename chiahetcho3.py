t = int(input())
for i in range(t) :
    s=input()
    check=0
    for j in s :
        check +=int(j)
    if check%3==0 :
        print("YES")
    else : print("NO")