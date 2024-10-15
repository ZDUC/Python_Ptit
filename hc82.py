class BA:
    def __init__(self, stk, sd, nm, ten):
        self.stk=stk
        self.sd=sd
        self.nm=nm
        self.ten=ten
    def nap(self, sd, stn):
        self.sd=sd + stn
    def rut(self ,sotr):
        if sotr>self.sd:
            print("so du khong du")
        else:
            self.sd=self.sd-sotr
    def kt(self):
        print("sd: "+str(self.sd))
a=BA("2502117103304",500,"11/07/2003","Zeros")
a.nap(500,34)
a.kt()
a.rut(600)
a.rut(117)
a.kt()