
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    
    res = 0
    pt = 0
    m = max(a)
    for x in a:
        if x == m:
            pt +=1
            res = max(res, pt)
        else:
            pt = 0
    print(res)