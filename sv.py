hscsattt = 3
hscsltmm = 3
hsathdh = 3
hsqlxdcs = 2
hsptpmud = 2
hsttcscn = 3
hsatcsdl = 2
sum_tin = 18
class sv:
    def __init__(self,sbd,hvt,atcsdl,athdh,csattt,csltmm,ptpmud,ttcscn,sqlxdcs,dtb):
        self.sbd = sbd
        self.hvt = hvt
        self.atcsdl = atcsdl*hsatcsdl
        self.athdh = athdh*hsathdh
        self.csatt = csattt*hscsattt
        self.csltmm = csltmm*hscsltmm
        self.ptpmud = ptpmud*hsptpmud
        self.ttcscn = ttcscn*hsttcscn
        self.sqlxdcs = sqlxdcs*hsqlxdcs
                
    def getDTB(self):
        self.dtb = (self.sbd + self.hvt + self.atcsdl + self.athdh + self.csatt + self.csltmm + self.ptpmud + self.ttcscn + self.sqlxdcs)/sum_tin
        return self.dtb

    