a = int(input())
for i in range(a):
  s = input()
  if len(s) < 2 : print("NO")
  else :
    if s[-2] == '8' and s[-1] == '6' : print("YES")
    else : print("NO")
  