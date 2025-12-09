class GiaDinh:
    def __init__(self,id, hoTen , loaiHo, csDau , csCuoi):
        self.id = f"KH{id:02d}"
        self.ten = self.chuanHoa(hoTen)
        self.loaiHo = loaiHo.strip()
        self.csDau = int(csDau)
        self.csCuoi = int(csCuoi)
        self.dinhMuc = self.tinhDinhMuc(loaiHo)
        self.soDien = self.csCuoi - self.csDau
        self.tienTrong = self.tinhTienTrongDinhMuc()
        self.tienNgoai = self.tinhTienNgoaiDinhMuc()
        self.thue = self.tinhThue()
        self.tongTienNop = self.tinhTienNop()


    def chuanHoa(self, tmp):
        x= tmp.lower().split()
        res = ""
        for y in x:
            res += y[0].upper() + y[1:] + " "
        return res.strip()
    
    def tinhDinhMuc(self, x):
        if x == "A": return 100
        elif x== "B": return 500
        return 200
    
    def tinhTienTrongDinhMuc(self):
        return min(self.dinhMuc, self.soDien) * 450
    
    def tinhTienNgoaiDinhMuc(self):
        if self.soDien > self.dinhMuc:
            return (self.soDien - self.dinhMuc) * 1000
        return 0
    
    def tinhThue(self):
        if self.tienNgoai > 0:
            return self.tienNgoai // 20
        return 0
        
    def tinhTienNop(self):
        return self.tienTrong + self.tienNgoai + self.thue
    
    def __str__ (self):
        return f"{self.id} {self.ten} {self.tienTrong} {self.tienNgoai} {self.thue} {self.tongTienNop}"
    
if __name__ == "__main__":
    n = int(input())
    ds = []
    for i in range(n):
        ten = input()
        loai, dau, cuoi = input().split() 
        ds.append(GiaDinh(i+1, ten, loai, dau, cuoi))
    ds.sort(key = lambda x : -x.tongTienNop)
    for x in ds:
        print(x)
