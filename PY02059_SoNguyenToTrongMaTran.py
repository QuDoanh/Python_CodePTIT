import math
def snt(x):
    if x<2:
        return False
    for i in range(2, math.isqrt(x) +1):
        if x % i == 0:
            return False
    return True    
    
if __name__ == "__main__":
    n , m = list(map(int, input().split()))
    a = [list(map(int, input().split())) for i in range(n)]

    vi_tri = []
    so_max = -1

    for i in range(n):
        for j in range(m):
            if snt(a[i][j]):
                if a[i][j] > so_max:
                    so_max = a[i][j]
                    vi_tri = [[i,j]]
                elif a[i][j] == so_max:
                    vi_tri.append([i,j])

    if not vi_tri:
        print("NOT FOUND")
    else:
        print(so_max)
        for x in vi_tri:
            print("Vi tri", end = " ")
            for y in x:
                print(f"[{y}]",end ="")
            print()

