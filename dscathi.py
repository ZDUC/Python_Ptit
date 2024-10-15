class Cathi(object):
    def __init__(self,ma,ngay,gio,phong):
        self.ma=ma
        self.ngay=ngay
        self.gio=gio
        self.phong=phong
    def __str__(self)->str:
        return f"{self.ma} {self.ngay} {self.gio} {self.phong}"
with open("CATHI.in",mode="r") as file:
    n=int(file.readline().strip())
    l=[]
    for i in range(1,n+1):
        ma="C"+str(i).zfill(3)
        ngay=file.readline().strip()
        gio=file.readline().strip()
        phong=file.readline().strip()
        l.append(Cathi(ma,ngay,gio,phong))
    l.sort(key=lambda exam: (exam.ngay,exam.gio,exam.ma))
    for i in l:
        print(i)