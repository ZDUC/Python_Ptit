import math
class ts():
    def __init__(self, ma, ten, tong, tt) :
        self.ma = ma
        self.ten = ten
        self.tong = tong
        self.tt = tt
    def __str__(self):
        return f"{self.ma} {self.ten}{round(self.tong, 1)} {self.tt}"
def diemcong(dt, kv):
    ks = 0
    if dt != "Kinh": ks += 1.5
    if kv == 3: ks +=  0
    if kv == 1: ks += 1.5
    if kv == 2: ks += 1
    if dt == "Kinh": ks += 0 
    return ks
def ch(ten):
    s=ten.split()
    tench=""
    for i in s:
        tench=tench+i[0].upper()+i[1::].lower()+" "
    return tench
t=int(input())
ds=[]
for i in range(t):
    ma="TS"+ str(i+1).zfill(2)
    ten=input()
    diem=float(input())
    dt=input()
    kv=int(input())
    diem=diem+diemcong(dt,kv)
    ten=ch(ten)
    if diem>=20.5: tt="Do"
    else : tt="Truot"
    ds.append(ts(ma, ten, diem, tt))
ds.sort(key=lambda x : x.tong, reverse=True)
for i in ds:
    print(i)
    