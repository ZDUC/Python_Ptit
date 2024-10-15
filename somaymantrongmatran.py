h,c,check,ma,mi=[],[],1,0,10**5
n,m=map(int,input().split())
for i in range(n):
    arr=list(map(int,input().split()))
    ma=max(ma,max(arr))
    mi=min(mi,min(arr))
    h.append(arr)
for i in range(n):
    for j in range(m):
        if h[i][j]==ma-mi:
            check=0
            c.append(f'Vi tri [{i}][{j}]')
if check==1: print('NOT FOUND')
else:
    print(ma-mi)
    print('\n'.join(c))
