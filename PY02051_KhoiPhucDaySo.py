if __name__ == "__main__":
    n = int(input())
    a = []

    b = [0]*n

    for i in range(n):
        row = list(map(int, input().split()))
        a.append(row)
    
    if(n == 2):
        if(a[0][1] % 2 == 0):
            b[0] = b[1] = a[0][1] //2
        else:
            b[0] = 1
            b[1] = a[0][1] - 1
    else:
        b[0] = (a[0][1] + a[0][2] - a[1][2])//2
        for i in range(1, n):
            b[i] = a[0][i] - b[0]
    
    for x in b:
        print(x, end = " ")
    print()