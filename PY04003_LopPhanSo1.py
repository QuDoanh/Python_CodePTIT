import math

class PhanSo:
    def __init__(self, tu , mau):
        self.tu = tu
        self.mau = mau
    
    def rutGon(self):
        ucln = math.gcd(self.mau, self.tu)
        self.tu //= ucln
        self.mau //= ucln

    def __str__(self):
        return f"{self.tu}/{self.mau}"


if __name__ == "__main__":
    x , y = map(int, input().split())
    p1 = PhanSo(x,y)
    p1.rutGon()
    print(p1)

