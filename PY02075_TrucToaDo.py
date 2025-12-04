
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a=[]
        for _ in range(n):
            b = list(map(int,input().split()))
            a.append(b)
        a.sort(key = lambda x : (x[1], x[0]))

        cnt = 1
        id_end = a[0][1]
        for i in range(1,n):
            if a[i][0] >= id_end:
                cnt+=1
                id_end = a[i][1]
        print(cnt) 

    