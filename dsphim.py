class DSPhim :
    def __init__(self, ma, tl, time, ten, st) :
        self.ma = 'P{:03d}'.format(ma)
        self.tl = tl
        self.ten = ten
        self.time = time
        self.ngay = int(time[0:2:])
        self.thang = int(time[3:5:])
        self.nam = int(time[6:None:])
        self.st = st
    def __str__(self) :
        return self.ma + ' ' + self.tl+ ' ' + self.time + ' ' + self.ten + ' ' + str(self.st)

n, m = map(int, input().split())
p = []
l=[]
for i in range(n) : 
    x=input()
    l.append(x)
for i in range(m) :
    ma = input()
    ngay = input()
    ten = input()
    st = int(input())
    p.append(DSPhim(i + 1, l[int(ma[2::]) - 1], ngay, ten, st))
p = sorted(p, key = lambda x : (x.nam, x.thang, x.ngay, x.ten, -x.st))
for i in range(m) :
    print(p[i])