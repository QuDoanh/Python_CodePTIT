if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    mul3 = a[-3]*a[-2]*a[-1]
    mul2 = a[-2]*a[-1]

    mul3_first = a[0]*a[1]*a[-1]
    mul2_first = a[0]*a[1]

    res = max(mul2, mul3, mul2_first, mul3_first)
    print(res)