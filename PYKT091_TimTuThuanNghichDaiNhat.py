def thuanNghich(x):
    return x == x[::-1]

if __name__ == "__main__":
    with open("VANBAN.in", "r") as f:
        data = f.read()
    tmp = data.split()
    res = []
    d = {}
    doDai = 0
    for i in range(len(tmp)):
        x = tmp[i]
        if thuanNghich(x):
            if x not in d:
                d[x] = 1
            else: d[x] +=1
            if x not in res:
                res.append(x)
            if len(x) > doDai:
                doDai = len(x)

    for x in res:
        if len(x) == doDai:
            print(f"{x} {d[x]}")
    