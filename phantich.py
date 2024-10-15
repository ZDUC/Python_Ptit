import math
for i in range(int(input())):
  n=int(input())
  print(1,end="")
  for j in range(2,int(math.sqrt(n))+1):
    if n%j==0:
      dem=0
      while n%j==0:
        if n%j==0:
          dem=dem+1
          n//=j
      print(" * "+str(j)+"^"+str(dem),end="")
  if n>1:
    print(" * "+str(n)+"^"+"1",end="")
  print()
