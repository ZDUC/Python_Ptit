ds=[1,0,10,6]
print(ds[::-1])
a,b=0,len(ds)-1
while a<b:
    ds[a],ds[b]=ds[b],ds[a]
    a=a+1
    b=b-1
print(ds)