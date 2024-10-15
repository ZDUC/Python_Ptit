ds=[1,2,3,4,5,6]
ds.append(7)
ds.insert(0,0)
del ds[0]
ds.pop(-1)
print(sorted(ds,reverse=True))
ds.sort(reverse=True)
print(len(ds))