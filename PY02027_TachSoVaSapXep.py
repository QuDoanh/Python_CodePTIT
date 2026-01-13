if __name__ == "__main__":
    n = int(input())
    res = []
    for _ in range(n):
        line = input()

        so = ""
        for ch in line:
            if ch.isdigit():
                so += ch
            else:
                if so != "":
                    x = int(so)
                    res.append(x)
                    so = ""

        if so != "":
            res.append(int(so))
    res.sort()
    for x in res:
        print(x)
