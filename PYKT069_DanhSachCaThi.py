class CaThi:
    def __init__(self,id, ngayThi, hThi, phongThi):
        self.id = f"C{id:03d}"
        self.ngayThi = ngayThi
        self.hThi = hThi
        self.phongThi = phongThi
        self.sx = self.cmp()

    def cmp(self):
        h, p = self.hThi.split(":")
        d, t, n = self.ngayThi.split("/")
        return (n, t,d, h, p)
    
    def __str__(self):
        return f"{self.id} {self.ngayThi} {self.hThi} {self.phongThi}"

if __name__ == "__main__":
    with open("CATHI.in") as f:
        data = f.read()
        s = data.split()
        ds = []
        i = 1
        cs = 1
        while(i<=int(s[0])):
            ds.append(CaThi(i, s[cs], s[cs+1], s[cs+2]))
            cs += 3
            i+=1
        ds.sort(key = lambda x: x.sx)
        for x in ds:
            print(x)
