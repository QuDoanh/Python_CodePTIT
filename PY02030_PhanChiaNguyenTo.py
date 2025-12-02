import math
def snt(x):
    if(x<2):
        return 0
    for i in range(2, math.isqrt(x)+1):
        if(x % i == 0):
            return 0
    return 1

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))

    b = []
    for x in a:
        if x not in b:
            b.append(x)        


    check = False
    for i in range(len(b)):
        sum1 = sum(b[0:i+1])
        sum2 = sum(b[i+1:])
        if(snt(sum1) and snt(sum2)):
            print(i)
            check = True
            break
    if not check:
        print("NOT FOUND")