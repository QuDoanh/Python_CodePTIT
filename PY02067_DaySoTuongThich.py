
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))

    res = 10**18
    m = min(a)

    for q in range(m+1):
        sum = 0 
        check = True

        for x in a:
            if q == 0:
                b = x+1
            else:
                b = x//(q+1) +1
                if b >x//q:
                    check = False
                    break
            sum += b
        if check:
            res = min(res, sum)
    print(res)