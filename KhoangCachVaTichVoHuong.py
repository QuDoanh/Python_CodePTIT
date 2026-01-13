import math
if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        X = list(map(int, input().split()))
        Y = list(map(int, input().split()))

        d = 0
        total = 0

        voHuong = 0
        for i in range(len(X)):
            tmp = Y[i] - X[i]
            total += tmp ** 2

            z = X[i] * Y[i]
            voHuong += z
        d = math.sqrt(total)


        print(f"{round(d, 2):.2f} {voHuong}")

