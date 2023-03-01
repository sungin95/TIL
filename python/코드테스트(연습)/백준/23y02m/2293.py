import sys

sys.stdin = open("2293.txt", "r")

n, k = map(int, input().split())
coin = []
for _ in range(n):
    data = int(input())
    coin.append(data)
coin.sort()
dp = [0] * (k + 1)
dp[0] = 1
# print(dp)

# 제일 값이 낮은 코인부터 차례로
for i in coin:
    for j in range(i, k + 1):
        dp[j] += dp[j - i]
print(dp[-1])
