dem=dict()
with open('C.txt') as filefuck:
    s=filefuck.read().replace(",","").replace(".","").split()
for i in s:
    try: dem[i]+=1
    except: dem[i]=1
print(dem)
    