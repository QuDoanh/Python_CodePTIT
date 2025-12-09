class DoiThi:
    def __init__(self, maTeam, ten, truong):
        self.id = maTeam
        self.tenTeam = ten
        self.truong = truong


class ThiSinh:
    def __init__(self, maTS, ten, teamObj):
        self.maTS= f"C{maTS:03d}"
        self.tenTS = ten
        self.team = teamObj

    def __str__(self):
        return f"{self.maTS} {self.tenTS} {self.team.tenTeam} {self.team.truong}"

if __name__ == "__main__":
    n = int(input())

    dsTeam_map = {}
    for i in range(n):
        team = input()
        truong = input()
        idTeam = f"Team{i+1:02d}"
        dsTeam_map[idTeam] = DoiThi(idTeam, team, truong)
    
    m = int(input())
    dsTS = []
    for i in range(m):
        ts = input()
        maTeam = input()

        teamObj = dsTeam_map[maTeam]
        dsTS.append(ThiSinh(i+1, ts, teamObj))
    dsTS.sort(key = lambda x : x.tenTS)
    for x in dsTS:
        print(x)