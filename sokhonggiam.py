t=int(input())
for i in range(t):
    s=input()
    check=0
    for j in range(len(s)-1):
        if s[j+1]<s[j]:
            check=1
            break
    if check==0: print("YES")
    else : print("NO")