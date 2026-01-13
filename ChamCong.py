class CongNhan:
    def __init__(self,ma, ten, vao, ve):
        self.ma = ma
        self.ten = ten
        self.vao = vao
        self.ve = ve
        self.tongPhut = self.tinhThoiGian()

    def tinhThoiGian(self):
        hVao, pVao = map(int, self.vao.split(":"))
        hVe, pVe = map(int, self.ve.split(":"))
        if pVe < pVao:
            h = hVe - hVao -1
            p =pVe + 60 - pVao
        else: 
            h = hVe - hVao
            p = abs(pVe - pVao)
        return h * 60 + p - 60
        
    def duThieu(self):
        if self.tongPhut >= 8 * 60:
            return "DU"
        return "THIEU"
    
    def timeLam(self):
        tmp = self.tongPhut
        h = tmp // 60
        p = tmp % 60
        return f"{h} gio {p} phut"
    def __str__(self):
        return f"{self.ma} {self.ten} {self.timeLam()} {self.duThieu()}"
    
if __name__ == "__main__":
    n = int(input())
    ds = []
    for _ in range(n):
        ma = input()
        ten = input()
        v = input()
        r = input()
        ds.append(CongNhan(ma, ten, v, r))
    ds.sort(key = lambda x : -x.tongPhut)
    for x in ds:
        print(x)

