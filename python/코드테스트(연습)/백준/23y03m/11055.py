import sys

sys.stdin = open("14003.txt", "r")

N = int(input())
num = list(map(int, input().split()))
dp = [-1] * N
dp[0] = num[0]
for i in range(1, N):
    dp[i] = num[i]
    for j in range(i):
        if dp[j] < dp[i]:
            dp[i] = max(dp[i], dp[j] + num[i])
print(max(dp))
