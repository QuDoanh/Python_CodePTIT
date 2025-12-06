
def chuyenDoi(x):
    if x > 10:
        return x/10
    return x

class NhanVien:
    def __init__(self, id, name, lt, th):
        self.id = id
        self.name = name
        self.lt = chuyenDoi(lt)
        self.th = chuyenDoi(th)
        self.diemTb = (self.lt + self.th) /2

    def xepLoai(self, x):
        if x < 5: return "TRUOT"
        elif x <8: return "CAN NHAC"
        elif x < 9.5: return "DAT"
        return "XUAT SAC"
    
    def __str__ (self):
        return f"TS0{self.id} {self.name} {self.diemTb:.2f} {self.xepLoai(self.diemTb)}"

if __name__ == "__main__":
    n = int(input())
    ds = []
    for i in range(n):
        ten = input()
        lt = float(input())
        th = float(input())
        ds.append(NhanVien(i+1, ten, lt, th))
    ds.sort(key = lambda x : -x.diemTb)
    for x in ds:
        print(x)