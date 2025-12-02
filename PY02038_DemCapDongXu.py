
if __name__ == "__main__":
    n = int(input())
    a = []
    res = 0
    for i in range(n):
        row = list(input())
        a.append(row)
    
    for i in range(n):
        cnt = 0
        for j in range(n):
            if a[i][j] == "C":
                cnt +=1
        res += cnt*(cnt-1)//2
    
    for j in range(n):
        cnt = 0
        for i in range(n):
            if(a[i][j] == "C"):
                cnt += 1
        res += cnt*(cnt -1)//2
    print(res)
