
def stn(x):
    if x < 10:
        return False
    s =str(x)
    return s == s[::-1]


if __name__ == "__main__":
    n , m = list(map(int, input().split()))
    a = [list(map(int, input().split())) for i in range(n)]

    so_max = 0
    vi_tri = []

    for i in range(n):
        for j in range(m):
            if stn(a[i][j]):
                if(a[i][j] > so_max):
                    so_max = a[i][j]
                    vi_tri = [[i,j]]
                elif a[i][j] == so_max:
                    vi_tri.append([i,j])
    
    if so_max == 0:
        print("NOT FOUND")
    else:
        print(so_max)
        for x in vi_tri:
            print("Vi tri", end = " ")
            for y in x: 
                print(f"[{y}]", end = "")
            print()