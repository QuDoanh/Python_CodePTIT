if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int , input().split()))
        cnt = [0] * 1000001

        res = None
        cnt_res = 0

        for x in a:
            cnt[x]+=1
            if(cnt[x] > cnt_res):
                cnt_res = cnt[x]
                res = x
        if cnt_res > n//2:
            print(res)
        else: print("NO")