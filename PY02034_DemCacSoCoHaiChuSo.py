if __name__ == "__main__":
    s = input()
    res = []
    cnt = [1]*100
    
    for i in range(0,len(s), 2):
        if(i + 2 <= len(s)):
            x = int(s[i] + s[i+1])
            if(x not in res):
                res.append(x)
            else:
                cnt[x] +=1
    
    for x in res:
        print(x, end= " ")
        print(cnt[x])