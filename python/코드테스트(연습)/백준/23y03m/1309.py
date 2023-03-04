N = int(input())

dp = [[0] * 3 for i in range(N)]
for j in range(3):
    dp[0][j] = 1

if N == 1:
    print(3)
else:
    for i in range(1, N):
        for j in range(3):
            dp[i][j] = (sum(dp[i - 1]) - dp[i - 1][j]) % 9901
        else:
            dp[i][0] += dp[i - 1][0]
    print(sum(dp[-1]) % 9901)
