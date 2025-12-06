def lamTron(x):
    tmp = x - int(x)
    if tmp < 0.5:
        return int(x)
    return int(x) +1

class KhachHang:
    def __init__(self, id, name, csCu, csMoi):
        self.id = id
        self.name = name
        self.csCu = csCu
        self.csMoi = csMoi
        self.cs = csMoi - csCu
        self.phuPhi = self.tinhPhuPhi(self.cs)
        self.tongTien = self.tinhTongTienNuoc(self.cs) * (self.phuPhi +1)

    def tinhTongTienNuoc(self, x):
        if x <= 50:
            return x * 100
        elif x<=100:
            return 5000 + (x-50)*150
        else: return 12500 + (x-100)*200
    
    def tinhPhuPhi(self, cs):
        if cs <= 50: return 0.02
        elif cs<=100: return 0.03
        return 0.05
    
    def __str__ (self):
        return f"KH{self.id:02d} {self.name} {lamTron(self.tongTien)}"
    
if __name__ == "__main__":
    n = int(input())
    ds = []
    for _ in range(n):
        name = input()
        cu = int(input())
        moi = int(input())
        ds.append(KhachHang(len(ds) +1, name, cu, moi))
    ds.sort(key = lambda x :(-x.tongTien))
    for x in ds:
        print(x)

    
