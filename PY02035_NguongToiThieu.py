
if __name__ == "__main__":
    s = input()
    k = int(input())
    res = []
    cnt = [1]*100

    for i in range(0, len(s), 2):
        if(i +2 <= len(s)):
            tmp = int(s[i] + s[i+1])
            if(tmp not in res):
                res.append(tmp)
            else:
                cnt[tmp]+=1
    
    res.sort()
    check = False
    for x in res:
        if(cnt[x] >= k):
            check = True
            print(x , end = " ")
            print(cnt[x])

    if not check:
        print("NOT FOUND")