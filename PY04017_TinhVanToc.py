
class VanDongVien:
    def __init__(self, ten, dv, denDich):
        
        self.ten = ten
        self.dv = dv
        self.denDich = denDich
        self.id = self.timId()
    
    def timId(self):
        res = ""
        dayDV = self.dv.split()
        dayTen = self.ten.split()
        for x in dayDV:
            res += x[0]
        for x in dayTen:
            res += x[0]
        return res
    
    def tinhH(self):
        h , p = map(int, self.denDich.split(':'))
        return (h-6) + p/60
    
    def vTB(self):
        tb = 120 / self.tinhH()
        return round(tb)
    
    def __str__(self):
        return f"{self.id} {self.ten} {self.dv} {self.vTB()} Km/h"
    
if __name__ == "__main__":
    n = int(input())
    ds = []
    for _ in range(n):
        ten= input()
        dc = input()
        h = input()
        ds.append(VanDongVien(ten, dc, h))
    
    ds.sort(key= lambda x : x.tinhH())
    for x in ds:
        print(x)