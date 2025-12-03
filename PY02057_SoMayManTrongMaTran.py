
if __name__ == "__main__":
    n , m = list(map(int, input().split()))
    a = [list(map(int, input().split())) for i in range(n)]

    vi_tri = []
    so_max = max(max(row) for row in a)
    so_min = min(min(row) for row in a)
    soMayMan = so_max  - so_min

    for i in range(n):
        for j in range(m):
            if a[i][j] == soMayMan:
                vi_tri.append([i,j])

    if not vi_tri:
        print("NOT FOUND")
    else:
        print(soMayMan)
        for x in vi_tri:
            print("Vi tri", end = " ")
            for y in x:
                print(f"[{y}]",end ="")
            print()

