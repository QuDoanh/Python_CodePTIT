
class MonHoc:
    def __init__(self, maMon, tenMon):
        self.maMon = maMon
        self.tenMon = tenMon

class LichThi:
    def __init__(self, monHoc, maCaThi, ngayThi, gioThi, nhomThi):
        self.monHoc = monHoc
        self.maCaThi = f"T{maCaThi:03d}"
        self.ngayThi = ngayThi
        self.gioThi = gioThi
        self.nhomThi = nhomThi

    def ngayThiCMP(self):
        d, m , y = map(int, self.ngayThi.split("/"))
        return (y, m, d)
    
    def gioThiCMP(self):
        hh , mm = map(int, self.gioThi.split(":"))
        return (hh, mm)
    
    def __str__(self):
        return f"{self.maCaThi} {self.monHoc.maMon} {self.monHoc.tenMon} {self.ngayThi} {self.gioThi} {self.nhomThi}"
    
if __name__ == "__main__":
    n , m = map(int, input().split())
    mon_map = {}
    for i in range(n):
        maMon = input()
        tenMon = input()
        mon_map[maMon] = MonHoc(maMon, tenMon)

    dsThi = []
    for i in range(m):
        maMonHoc, ngay, h, nhom = input().split()
        monObj = mon_map[maMonHoc]
        dsThi.append(LichThi(monObj ,i+1, ngay, h , nhom))
    
    dsThi.sort(key = lambda x : (x.ngayThiCMP(), x.gioThiCMP(), x.monHoc.maMon))
    for x in dsThi:
        print(x)

    