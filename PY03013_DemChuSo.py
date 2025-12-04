

def cnt(n , d):
    if(n<0):
        return 0
    if n == 0: return 0

    count = 0

    p = 1
    while(p <=n ):
        a = n//p
        left = a//10
        cur = a%10
        right = n % p

        if d != 0:
            count += left * p
        else:
            count += (left - 1) * p

        if cur > d:
            count += p
        elif cur == d:
            count += right +1
        
        p *= 10
    return count 

if __name__ == "__main__":
    t= int(input())
    for _ in range(t):
        a , b = map(int, input().split())
        res = []
        for d in range(10):
            ans = cnt(b, d) - cnt(a-1, d)
            res.append(ans)
        for x in res:
            print(x, end = " ")
        print()