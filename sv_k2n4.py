import math
hsdgkd = 3
hspttkat = 2
hsttpt = 3
hsatmmt = 4
hsgtatm = 2
hsktgt = 2

sum_tin = 16
class sv:
    def __init__(self,hvt,sbd,dgkd,pttkat,ttpt,atmmt,gtatm,ktgt):
        self.sbd = sbd
        self.hvt = hvt
        self.dgkd = dgkd
        self.pttkat = pttkat
        self.ttpt = ttpt
        self.atmmt = atmmt
        self.gtatm = gtatm
        self.ktgt = ktgt
                
    def getDTB(self):
        db = (self.dgkd*hsdgkd + self.pttkat*hspttkat + self.ttpt*hsttpt + self.atmmt*hsatmmt + self.gtatm*hsgtatm + self.ktgt*hsktgt)/sum_tin
        return round(db, 2)
        
    def toString(self):
        return self.sbd + ' ' + self.hvt + ' ' + str(self.dgkd) + ' ' + str(self.pttkat) + ' '+ ' ' + str(self.atmmt) + ' ' + str(self.gtatm) + ' ' + str(self.ktgt) + ' ' + str(self.getDTB())
    