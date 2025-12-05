

if __name__ == "__main__":
    n = int(input())
    d = {}
    for _ in range(n-1):
        x,y = map(int, input().split())
        d[x] = d.get(x, 0) +1
        d[y] = d.get(y, 0) +1
     
    if (n-1) in d.values():
        print("Yes")
    else:
        print("No")
