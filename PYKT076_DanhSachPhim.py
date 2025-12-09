
class BoPhim:
    def __init__(self, maP, tenP, khoiChieu, soTap, TheLoai):
        self.maP = f"P{maP:03d}"
        self.tenP = tenP
        self.khoiChieu = khoiChieu
        self.khoiChieuCMP = self.chuyenNgayKhoiChieu(khoiChieu)
        self.soTap = soTap
        self.theLoai = TheLoai

    def chuyenNgayKhoiChieu(self, x):
        d, m, y = x.split('/')
        return (y,m,d)

    def __str__(self):
        return f"{self.maP} {self.theLoai} {self.khoiChieu} {self.tenP} {self.soTap}"
    
class TheLoai:
    def __init__(self, maTL, tenTL):
        self.maTL = f"TL{maTL:03d}"
        self.tenTL = tenTL

if __name__ == "__main__":
    n , m = map(int, input().split())
    dsTL = {}
    dsP = []
    for i in range(n):
        tenTL = input()
        tl = TheLoai(i+1, tenTL)
        dsTL[tl.maTL] = tl.tenTL

    for i in range(m):
        maTL = input()
        kc = input()
        tenP = input()
        soTap = int(input())

        tenTL = dsTL[maTL]
        dsP.append(BoPhim(i+1, tenP, kc, soTap, tenTL))
    dsP.sort(key = lambda x : (x.khoiChieuCMP, x.tenP, -x.soTap))
    for x in dsP:
        print(x)