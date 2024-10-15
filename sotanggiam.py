def check(s) :
    if len(s)<3: return 0
    if s[1] <= s[0] or s[-2] <= s[-1] : return 0
    p1 = 1
    p2 = len(s) - 2
    while s[p1] > s[p1 - 1] and p1 < len(s) : p1 += 1
    while s[p2] > s[p2 + 1] and p2 >= 0 : p2 -= 1
    if p1 == p2 + 2 : return 1
    else : return 0
t = int(input())
for i in range(t) :
    s = input()
    if check(s) == 1 : print("YES")
    else : print("NO")