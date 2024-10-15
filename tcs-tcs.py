
t=int(input())
for i in range(t):
    s=input()
    tong=0
    tich=1
    check=0
    for j in range(len(s)):
        if j%2==0: tong+=int(s[j])
        else:
            if s[j]!='0': 
                tich*=int(s[j])
                check=1
    if check==0: tich=0
    print(tong, end=" ")
    print(tich)