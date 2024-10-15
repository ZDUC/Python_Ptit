import math
def nto(n) :
    if n < 2 : return 0
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0 : return 0
    return 1
t = int(input())
for i in range(t) :
    n = int(input())
    s = 0
    for i in range(1, n) :
        if math.gcd(i, n) == 1 : s += 1
    if nto(s) == 1 : print("YES")
    else : print("NO")