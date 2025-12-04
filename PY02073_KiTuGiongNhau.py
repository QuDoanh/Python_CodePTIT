
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        x, y , z = map(int, input().split())

        dp = [10**9] * (n+1)
        dp[0] = 0
        dp[1] = x

        for i in range(2, n+1):
            dp[i] = min(dp[i], dp[i-1] + x)

            if i % 2 == 0:
                dp[i] = min(dp[i], dp[i//2] + z)
            else:
                dp[i] = min(dp[i], dp[(i+1)//2] + z + y)
        print(dp[n])

    