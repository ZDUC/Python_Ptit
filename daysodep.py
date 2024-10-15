t=int(input())
for t in range(t):
    n, A = int(input()), list(map(int, input().split()))
    dem = 0
    for i in range(n-1):
        mi = min(A[i], A[i+1])
        ma = max(A[i], A[i+1])
        while ma>mi*2: 
            dem=dem+1
            mi=mi*2
    print(dem)