import sys

sys.stdin = open("9251.txt", "r")
x = list(input())
y = list(input())


dp = [[0] * (len(x) + 1) for i in range(len(y) + 1)]
max_num = 0
for i in range(1, len(y) + 1):
    for j in range(1, len(x) + 1):
        if y[i - 1] == x[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            if max_num < dp[i][j]:
                max_num = dp[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            if max_num < dp[i][j]:
                max_num = dp[i][j]
print(max_num)
