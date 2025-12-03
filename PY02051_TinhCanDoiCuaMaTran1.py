

if __name__ == "__main__":
    n = int(input())
    a= []

    for i in range(n):
        row = list(map(int, input().split()))
        a.append(row)

    k = int(input())

    sum_on = 0
    sum_under = 0
    for i in range(n):
        for j in range(n):
            if(i != j):
                if(j > i):
                    sum_on += a[i][j]
                else:
                    sum_under += a[i][j]
    
    res = sum_on - sum_under
    if res <= k:
        print("YES")
    else:
        print("NO")

    print(abs(res))
