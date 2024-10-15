t=int(input())
for i in range(t) :
    s=input()
    check=1
    for j in s:
        if j!='0' and j!='1' and j!='2' : 
            print("NO")
            check=0
            break
    if check==1 : print("YES")