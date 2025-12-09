
class ThiSinh:
    def __init__(self, id, name, diemThi, dt, kv):
        self.id = f"TS{id:02d}"
        self.name= self.chuanHoaTen(name)
        self.diemThi = diemThi
        self.danToc = dt
        self.khuVuc = kv
        self.tongDiem = round(self.diemThi + self.tinhDiemUuTien(), 1)

    def chuanHoaTen(self, x):
        x = x.lower().split()
        res = ""
        for i in x:
            res += i[0].upper() + i[1:]
            res += " "
        return res.strip()
    
    def tinhDiemUuTien(self):
        res = 0
        if self.danToc == "Kinh":
            res += 0
        else:
            res += 1.5

        if self.khuVuc == 1:
            res += 1.5
        elif self.khuVuc == 2: res += 1
        else: res+=0
        return res
    
    def trangThai(self):
        if self.tongDiem >= 20.5:
            return "Do"
        return "Truot"

    def __str__ (self):
        return f"{self.id} {self.name} {self.tongDiem} {self.trangThai()}"
    
if __name__ == "__main__":
    n = int(input())
    ds  = []
    for i in range(n):
        ten = input()
        diemThi = float(input())
        dt = input()
        kv = int(input())
        ds.append(ThiSinh(i+1, ten , diemThi, dt, kv))
    ds.sort(key = lambda x : (-x.tongDiem, x.id) )
    for x in ds:
        print(x)
