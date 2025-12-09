class PhongBan:
    def __init__(self, maPB, tenPB):
        self.maPB = maPB.strip()
        self.tenPB = tenPB.strip()

class NhanVien:
    def __init__(self, maNV, ten, luongCB, ngayCong, phongBanObj):
        self.maNV = maNV
        self.ten = ten
        self.luongCB = luongCB
        self.ngayCong = ngayCong
        self.phongBan = phongBanObj

        self.nhomNV = self.maNV[0]
        self.soNam = self.maNV[1:3]
        self.maPB = self.maNV[3:]
        self.heSo = self.heSoNhan()
        self.luongThang = self.luongCB * self.ngayCong *self.heSo * 1000

    def heSoNhan(self):
        nam = int(self.soNam)
        nhom = self.nhomNV

        if nam >= 1 and nam <=3:
            if nhom == "A" or nhom == "B":
                return 10
            elif nhom == "C":
                return 9
            return 8
        elif nam >= 4 and nam <=8:
            if nhom == "A":
                return 12
            elif nhom == "B": return 11
            elif nhom == "C":
                return 10
            return 8
        elif nam >=9 and nam <= 15:
            if nhom == "A": return 14
            elif nhom == "B": return 13
            elif nhom == "C":
                return 12
            return 11
        else:
            if nhom == "A": return 20
            elif nhom == "B": return 16
            elif nhom == "C":
                return 14
            return 13
    def __str__(self):
        return f"{self.maNV} {self.ten} {self.phongBan.tenPB} {self.luongThang}"
        
if __name__ == "__main__":
    n = int(input())
    dsPB = {}
    for i in range(n):
        line = input()
        cs = line.find(" ")
        dsPB[line[:cs]] = PhongBan(line[:cs], line[cs:])
    
    m = int(input())
    dsNV =[]
    for i in range(m):
        manv = input()
        ten = input()
        cb = int(input())
        ngayC = int(input())

        maP = manv[3:]
        phongBanObj = dsPB[maP]
        dsNV.append(NhanVien(manv, ten, cb, ngayC, phongBanObj))
    
    for x in dsNV:
        print(x)
         