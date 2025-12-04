
def soThuanNghich(x):
    x = str(x)
    if len(x) < 2:
        return False
    return x == x[::-1]

if __name__ == "__main__":
    n , m  = map(int, input().split())
    a = []

    for i in range(n):
        row = list(map(int,input().split()))
        a.append(row)

    viTri = []
    soMax = -1 
    
    for i in range(n):
        for j in range(m):
            if soThuanNghich(a[i][j]):
                if(a[i][j] > soMax):
                    viTri = [[i,j]]
                    soMax = a[i][j]
                elif a[i][j] == soMax:
                    viTri.append([i,j])
    if soMax == -1:
        print("NOT FOUND")
    else:
        print(soMax)
        for i, j in viTri:
            print(f"Vi tri [{i}][{j}]")
