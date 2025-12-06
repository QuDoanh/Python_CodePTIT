
class GiaoVien:
    def __init__ (self,id, ten, ma, tin, chuyenMon):
        self.id = id
        self.ten = ten
        self.ma = ma
        self.tin = tin
        self.chuyenMon = chuyenMon

    def diemUuTien(self):
        x = self.ma[1]
        if x == '1':
            return 2.0
        elif x == '2': return 1.5
        elif x == '3': return 1.0
        return 0
    
    def monHoc(self):
        x = self.ma[0]
        if x == "A": return "TOAN"
        elif x == "B": return "LY"
        return "HOA"
    
    def tongDiem(self):
        res = self.chuyenMon + self.tin * 2 + self.diemUuTien()
        return res
    
    def ketQua(self):
        if self.tongDiem() >= 18:
            return "TRUNG TUYEN"
        return "LOAI"
    
    def __str__(self):
        return f"GV{self.id:02d} {self.ten} {self.monHoc()} {self.tongDiem():.1f} {self.ketQua()}"
    
if __name__ == "__main__":
    n = int(input())
    ds = []
    for i in range(n):
        ten = input()
        ma = input()
        tin = float(input())
        cm = float(input())
        ds.append(GiaoVien(i+1, ten, ma, tin ,cm))
    ds.sort(key = lambda x : -x.tongDiem())
    for x in ds:
        print(x)