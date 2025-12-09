def lamTron(x):
    tmp = x - int(x)
    if tmp >= 0.5:
        return int(x) +1
    return int(x)

class SinhVien:
    def __init__(self, msv, name, d1, d2, d3):
        self.msv = f"SV{msv:02d}"
        self.name = self.chuanHoaTen(name)
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.xepHang = None
    
    def chuanHoaTen(self,x):
        x = x.lower().split()
        res = ""
        for tmp in x:
            res += tmp[0].upper() + tmp[1:] + " "
        return res.strip()
    
    def tinhTB(self):
        res = self.d1 * 3 + self.d2 * 3 + self.d3 * 2
        res /= 8
        return res
    
    def __str__ (self):
        return f"{self.msv} {self.name} {lamTron(self.tinhTB()* 100)/100:.2f} {self.xepHang}"
    
if __name__ == "__main__":
    n = int(input())
    ds =[]
    for i in range(n):
        ten = input()
        d1 = float(input())
        d2 = float(input())
        d3 = float(input())
        ds.append(SinhVien(i+1, ten, d1, d2, d3))
    ds.sort(key = lambda x : (-x.tinhTB(), x.msv))

    ds[0].xepHang = 1
    rank = 1
    for i in range(1,n):
        if(ds[i].tinhTB() == ds[i-1].tinhTB()):
            ds[i].xepHang = rank
        else:
            rank = i+1
            ds[i].xepHang = rank
    for x in ds:
        print(x)