
def tinhTime(x, y):
    tongPhutX = int(x[:2]) * 60 + int(x[3:])
    tongPhutY = int(y[:2]) * 60 + int(y[3:])
    tongTime = tongPhutY - tongPhutX
    return tongTime

class LuongMua:

    def __init__ (self,id, tenTram, batDau, ketThuc, luongDoDuoc):
        self.id = id
        self.tenTram = tenTram
        self.tongTime = tinhTime(batDau , ketThuc)
        self.tongLuongMua = luongDoDuoc

    def update(self, batDau , ketThuc, luongDoDuoc):
        self.tongTime += tinhTime(batDau, ketThuc)
        self.tongLuongMua += luongDoDuoc

    def __str__ (self):
        return f"T{self.id:02d} {self.tenTram} {(self.tongLuongMua / self.tongTime *60):.2f}"
    
if __name__ == "__main__":
    n = int(input())
    a = []
    for i in range(n):
        name = input()
        bd = input()
        kt = input()
        luongMua = int(input())

        checkTen = -1
        for j in range(len(a)):
            if name == a[j].tenTram:
                checkTen = j
                break
        
        if checkTen == -1:
            a.append(LuongMua(len(a)+1, name, bd, kt, luongMua))
        else:
            a[checkTen].update(bd, kt, luongMua)

    for x in a:
        print(x)

