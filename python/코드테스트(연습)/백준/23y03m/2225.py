N, K = map(int, input().split())

dp = [[0] * (K + 1) for i in range(N + 1)]


dp[0][0] = 1
for i in range(1, K + 1):
    dp[0][i] = 1
    for j in range(1, N + 1):
        dp[j][i] = dp[j][i - 1] + dp[j - 1][i]
print(dp[-1][-1] % 1000000000)
