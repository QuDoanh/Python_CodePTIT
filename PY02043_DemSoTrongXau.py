
if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        s = input()
        t = input()
        i = 0
        cnt = 0
        while i + len(t) <= len(s):
            if s[i:i+len(t)] == t:
                cnt+=1
                i+=len(t)
            else:
                i+=1
        print(cnt)