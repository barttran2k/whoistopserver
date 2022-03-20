hsatcsdl = 2
hscsltmm = 3
hscsattt = 3
hsathdh = 3
hsqlxdcs = 2
hsptpmud = 2
hsttcscn = 3

sum_tin = 18
class sv:
    def __init__(self,hvt,sbd,atcsdl,athdh,csattt,csltmm,ptpmud,ttcscn,qlxdcs):
        self.sbd = sbd
        self.hvt = hvt
        self.atcsdl = atcsdl
        self.athdh = athdh
        self.csatt = csattt
        self.csltmm = csltmm
        self.ptpmud = ptpmud
        self.ttcscn = ttcscn
        self.qlxdcs = qlxdcs
                
    def getDTB(self):
        db = (self.atcsdl*hsatcsdl + self.athdh*hsathdh + self.csatt*hscsattt + self.csltmm*hscsltmm + self.ptpmud*hsptpmud + self.ttcscn*hsttcscn + self.qlxdcs*hsqlxdcs)/sum_tin
        return round(db, 2)
        

    