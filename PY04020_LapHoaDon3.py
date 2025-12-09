
class MatHang:
    def __init__(self, id, ten, soLuong, donGia, chietKhau):
        self.id = id
        self.ten = ten
        self.soLuong = soLuong
        self.donGia = donGia
        self.chietKhau = chietKhau

    def tongTien(self):
        res = self.donGia * self.soLuong - self.chietKhau
        return res
    
    def __str__(self):
        return f"{self.id} {self.ten} {self.soLuong} {self.donGia} {self.chietKhau} {self.tongTien()}"
    
if __name__ == "__main__":
    n = int(input())
    ds =[]
    for i in range(n):
        id = input()
        ten = input()
        sl = int(input())
        gia = int(input())
        ck = int(input())
        ds.append(MatHang(id, ten, sl, gia, ck))
    ds.sort(key = lambda x : -x.tongTien())
    for x in ds:
        print(x)