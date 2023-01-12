import sys

sys.stdin = open("12865.txt", "r")

# 냅색 알고리즘 파이썬

N, K = map(int, input().split())

max_ = 0
items = [(0, 0)]
for _ in range(N):
    a, b = map(int, input().split())
    items.append((a, b))

dp = []
for i in range(N + 1):
    dp.append([])
    for j in range(K + 1):
        dp[-1].append(0)


for i in range(1, N + 1):
    for j in range(1, K + 1):
        if items[i][0] <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - items[i][0]] + items[i][1])
            if max_ < dp[i][j]:
                max_ = dp[i][j]
        else:
            dp[i][j] = dp[i - 1][j]
            if max_ < dp[i][j]:
                max_ = dp[i][j]
# print(dp)
print(max_)
