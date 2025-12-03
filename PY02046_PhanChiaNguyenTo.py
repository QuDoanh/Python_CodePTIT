import math

def snt(x):
    if(x<2):
        return False
    for i in range(2, math.isqrt(x)+1):
        if x%i == 0:
            return False
    return True


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    b  = []

    for x in a:
        if x not in b:
            b.append(x)
    
    total = sum(b)

    check = False
    for i in range(1, len(b)):
        sum1 = sum(b[:i])
        if snt(sum1) and snt(total - sum1):
            print(i-1)
            check = True
            break
    if not check:
        print("NOT FOUND")

    