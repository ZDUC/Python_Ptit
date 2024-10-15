s=input()
l=len(s)-1
ds=""
dem=0
while 1:
  ds=s[l]+ds
  if l==0: break
  dem=dem+1
  if dem==3:
    ds=","+ds
    dem=0
  l=l-1
print(ds)