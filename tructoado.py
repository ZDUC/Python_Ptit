class TTD :
    def __init__(self, x, y) :
        self.x = x
        self.y = y
for i in range(int(input())) :
    n = int(input())
    X = []
    for j in range(n) :
        x, y = map(int, input().split())
        X.append(TTD(x, y))
    X = sorted(X, key = lambda z : z.y)
    k,d = X[0].y, 1
    for o in range(1, n) :
        if X[o].x >= k :
            d = d+1
            k = X[o].y
    print(d)
