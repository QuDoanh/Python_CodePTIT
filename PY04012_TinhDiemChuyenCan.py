
class SinhVien:
    def __init__ (self, id, name , lop):
        self.id = id 
        self.name = name
        self.lop = lop 
        self.ghiChu = ""


    # def getId(self):
    #     return self.id

    # def getGhiChu(self):
    #     return self.ghiChu 

    # def setGhiChu(self, x):
    #     return self.ghiChu = x   

    def tinhDiemCC(self):
        res = 10
        for x in self.ghiChu:
            if x == 'v':
                res -= 2
            elif x == 'm' : res -= 1
            else: continue
        if res < 0: return 0
        return res
    
    def __str__(self):
        if self.tinhDiemCC() > 0:
            return f"{self.id} {self.name} {self.lop} {self.tinhDiemCC()}"
        return f"{self.id} {self.name} {self.lop} {self.tinhDiemCC()} KDDK"
        
if __name__ == "__main__":
    n  = int(input())
    ds = []
    for _ in range(n):
        id = input()
        name = input()
        lop = input()
        ds.append(SinhVien(id, name ,lop))
    for _ in range(n):
        x, y = input().split()
        for t in ds:
            if t.id == x:
                t.ghiChu = y
                break
    
    for x in ds:
        print(x)
