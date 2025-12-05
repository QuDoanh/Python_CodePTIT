import math

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def tinhTong(self, p2):
        mauChung = self.mau * p2.mau
        tuChung = self.tu * p2.mau + p2.tu*self.mau
        return PhanSo(tuChung, mauChung)

    def rutGon(self):
        ucln = math.gcd(self.tu, self.mau)
        self.tu //= ucln
        self.mau //=ucln
    
    def __str__(self):
        return f"{self.tu}/{self.mau}"
    
if __name__ == "__main__":
    t1, m1, t2,m2 = map(int, input().split())
    p1 = PhanSo(t1, m1)
    p2 = PhanSo(t2, m2)
    p = p1.tinhTong(p2)
    p.rutGon()
    print(p)
