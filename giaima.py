t=int(input())
for i in range(t):
    s=input()
    for j in range(0,len(s)-1,2):
        p=int(s[j+1])
        for k in range(p):
            print(s[j],end="")
    print()