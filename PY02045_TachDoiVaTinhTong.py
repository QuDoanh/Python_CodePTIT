def tachTinhTong(x):
    if(int(x)<10):
        return

    mid = len(x)//2
    a = int(x[: mid])
    b = int(x[mid : ])
    res = a+b
    print(res)
    tachTinhTong(str(res))

if __name__ == "__main__":
    s = input()
    tachTinhTong(s)
