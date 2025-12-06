
def chuyenDoi(x):
    h = int(x[:2])
    p = int(x[3:])
    return h * 60 + p

class NguoiChoi:
    def __init__ (self, id, name, hVao, hRa):
        self.id = id 
        self.name = name
        self.hVao = chuyenDoi(hVao) 
        self.hRa = chuyenDoi(hRa)
        self.tongH = self.hRa - self.hVao

    def tinhTongH(self):
        hh = self.tongH // 60
        mm = self.tongH  % 60
        return f"{hh} gio {mm} phut"
    
    def __str__ (self):
        return f"{self.id} {self.name} {self.tinhTongH()}"
    
if __name__ == "__main__":
    n = int(input())
    ds = []
    for _ in range(n):
        id = input()
        name = input() 
        v = input()
        r = input()
        ds.append(NguoiChoi(id, name, v, r))

    ds.sort(key = lambda x : -x.tongH)
    for x in ds:
        print(x)