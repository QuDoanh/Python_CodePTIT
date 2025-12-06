import sys

class ThiSinh:
    def __init__ (self, name, date, d1, d2, d3):
        self.name = name
        self.date = date
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3

    def tongDiem(self):
        return self.d1 + self.d2 + self.d3
    
    def chuanHoa(self, x):
        if x[1] == '/': x = '0' + x 
        if x[4] == '/': x = x[:3] + '0'+ x[3:]
        return x

    def __str__(self):
        return f"{self.name} {self.chuanHoa(self.date)} {self.tongDiem():.1f}"    
    

if __name__ == "__main__":
    name = input().strip()
    date = input().strip()
    d1 = float(input())
    d2 = float(input())
    d3 = float(input())
    ts = ThiSinh(name, date ,d1, d2, d3)
    print(ts)