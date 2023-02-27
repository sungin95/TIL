N = int(input())

dp = [[0] * 10 for i in range(N)]

for i in range(10):
    dp[0][i] = 1


for i in range(1, N):
    for k in range(10):
        for j in range(k + 1):
            dp[i][k] += dp[i - 1][j]

print(sum(dp[-1]) % 10007)
