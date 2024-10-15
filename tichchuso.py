t=int(input())
for i in range(t):
    s=input()
    check=1
    for j in s:
        if j!='0' : check=check*int(j)
    print(check)