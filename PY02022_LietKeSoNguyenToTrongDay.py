import math

def snt(x):
    if(x<2):
        return 0
    for i in range(2, math.isqrt(x) + 1):
        if(x % i == 0):
            return 0
    return 1

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0]*1000001

    thuTu = []
    for x in a:
        if(snt(x)):
            if(cnt[x] == 0):
                thuTu.append(x)
            cnt[x]+=1
    for x in thuTu:
        print(x, cnt[x])