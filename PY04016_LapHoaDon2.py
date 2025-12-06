from datetime import datetime

class KhachHang:
    def __init__ (self, id , ten, soP, ngayNhan, ngayTra, tienDV):
        self.id = id
        self.ten = ten 
        self.soP = soP
        self.ngayNhan = datetime.strptime(ngayNhan.strip(), "%d/%m/%Y").date() 
        self.ngayTra = datetime.strptime(ngayTra.strip(), "%d/%m/%Y").date()
        self.tienDV = tienDV
        self.thanhTien = self.tinhThanhTien()

    def soNgay(self):
        return (self.ngayTra - self.ngayNhan).days +1
    
    def tinhThanhTien(self):
        tang = self.soP // 100
        ngay = self.soNgay()
        if tang == 1:
            return 25 * ngay + self.tienDV
        elif tang == 2:
            return 34 * ngay + self.tienDV
        elif tang == 3:
            return 50 * ngay + self.tienDV
        return 80 * ngay + self.tienDV
    
    def __str__ (self):
        return f"KH{self.id:02d} {self.ten} {self.soP} {self.soNgay()} {self.thanhTien}"
    
if __name__ == "__main__":
    n = int(input())
    ds = []
    for i in range(n):
        ten = input()
        p = int(input())
        nhan = input()
        tra = input()
        dv = int(input())
        ds.append(KhachHang(i+1, ten, p, nhan ,tra, dv))

    ds.sort(key = lambda x : -x.thanhTien)
    for x in ds:
        print(x)