hh, mm, a, b = map(int, input().split())

tmp = abs(a-b)

if(a>b): hh = hh -tmp
else: hh = hh+tmp

if(hh>=24): hh=hh -24
if(hh<0): hh =hh+24
print(hh,mm)
