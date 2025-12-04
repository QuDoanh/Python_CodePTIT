

res = []
arr = []
def back(tongConThieu, tmp):
    if tongConThieu == 0:
        res.append(arr.copy())
        return
    for x in range(min(tongConThieu, tmp), 0, -1):
        arr.append(x)
        back(tongConThieu - x, x)
        arr.pop()
    return res

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        res = []
        arr = []
        back(n,n)
        print(len(res))
        for x in res:
            print("(", end = "")
            for y in range(len(x)):
                if(y != len(x) -1):
                    print(x[y], end = " ")
                else:
                    print(x[y], end = "")
            print(")", end = " ")
        print()

