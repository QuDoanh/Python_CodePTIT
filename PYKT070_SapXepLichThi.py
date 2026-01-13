class MonHoc:
    def __init__(self, maMon, tenMon, hinhThucThi):
        self.maMon = maMon
        self.tenMon = tenMon
        self.hinhThucThi = hinhThucThi


class CaThi:
    def __init__(self, maCaThi, ngayThi, hThi, phongThi):
        self.maCaThi = f"C{maCaThi:03d}"
        self.ngayThi = ngayThi
        self.hThi = hThi
        self.phongThi = phongThi
    
    def cmp(self):
        d, t, n = map(int, self.ngayThi.split("/"))   
        h, p = map(int, self.hThi.split(":"))         
        return (n, t, d, h, p, self.maCaThi)


class LichThi:
    def __init__(self, maCaThi, maMon, maNhom, soSV, caThiObj, monHocObj):
        self.maCaThi = maCaThi
        self.maMon = maMon
        self.maNhom = maNhom
        self.soSV = soSV
        self.caThi = caThiObj
        self.monHoc = monHocObj

    def __str__(self):
        return f"{self.caThi.ngayThi} {self.caThi.hThi} {self.caThi.phongThi} {self.monHoc.tenMon} {self.maNhom} {self.soSV}"


if __name__ == "__main__":
    # MONTHI.in
    with open("MONTHI.in", "r", encoding="utf-8") as f:
        m = int(f.readline().strip())
        m_monHoc = {}
        for _ in range(m):
            maMon = f.readline().strip()
            tenMon = f.readline().strip()
            hinhThucThi = f.readline().strip()
            m_monHoc[maMon] = MonHoc(maMon, tenMon, hinhThucThi)

    # CATHI.in
    with open("CATHI.in", "r", encoding="utf-8") as f:
        n = int(f.readline().strip())
        m_caThi = {}
        for i in range(1, n + 1):
            ngayThi = f.readline().strip()
            hThi = f.readline().strip()
            phongThi = f.readline().strip()
            ca = CaThi(i, ngayThi, hThi, phongThi)
            m_caThi[ca.maCaThi] = ca

    # LICHTHI.in
    with open("LICHTHI.in", "r", encoding="utf-8") as f:
        k = int(f.readline().strip())
        ds = []
        for _ in range(k):
            line = f.readline().strip()
            if not line:
                continue
            maCaThi, maMon, maNhom, soSV = line.split()
            ds.append(
                LichThi(
                    maCaThi, maMon, maNhom, soSV,
                    m_caThi[maCaThi],
                    m_monHoc[maMon]
                )
            )

    ds.sort(key=lambda x: x.caThi.cmp())
    for x in ds:
        print(x)
