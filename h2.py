dic1 = {
'aeinstein': 
{
'first': 'albert',
'last': 'einstein',
'location': 'princeton',
},
'mcurie': 
{
'first': 'marie',
'last': 'curie',
'location': 'paris',
},
'aeinstein1': 
{
'first': 'albert',
'last': 'einstein',
'location': 'princeton',
},
}
dic2 = {}
for i,j in dic1.items():
    if j not in dic2.values():
        dic2[i] = j
print(dic2)