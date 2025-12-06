
def lamTron(x):
    tmp = x - int(x)
    if(tmp < 0.5): return int(x)
    return int(x) + 1

class ThiSinh:
    def __init__(self, id, name, diemList):
        self.id = id
        self.name = name
        self.diem = diemList
        self.diemTb = self.tinhTB(self.diem)

    def tinhTB(self, diemList):
        tmp = sum(diemList[:2]) + sum(diemList)
        return tmp/12
    
    def xepLoai(self, diemTb):
        if diemTb >= 9: return "XUAT SAC"
        elif diemTb >= 8: return "GIOI"
        elif diemTb >= 7: return "KHA"
        elif diemTb >= 5: return "TB"
        return "YEU"
    
    def __str__(self):
        return f"HS{self.id:02d} {self.name} {lamTron(self.diemTb*10)/10:.1f} {self.xepLoai(self.diemTb)}"
    
if __name__ == "__main__":
    n = int(input())
    ds = []
    for _ in range(n):
        name = input()
        a = list(map(float, input().split()))
        ds.append(ThiSinh(len(ds) +1, name, a))
    
    ds.sort(key= lambda x : (-x.diemTb, x.id))
    for x in ds:
        print(x)
    
