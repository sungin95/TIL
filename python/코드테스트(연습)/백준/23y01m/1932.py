import sys

sys.stdin = open("1932.txt", "r")
from pprint import pprint

N = int(input())
triangle = []
dp = [[0]]
for i in range(N):
    data = list(map(int, input().split()))
    triangle.append(data)
    dp.append([])
    dp[-1] = [0] * (len(data) + 1)
# print(triangle)
# print(dp)
for i in range(N):
    for j in range(len(triangle[i])):
        if j == 0:
            dp[i + 1][j] = dp[i][j] + triangle[i][j]
        else:
            dp[i + 1][j] = max(dp[i][j], dp[i][j - 1]) + triangle[i][j]
# pprint(dp)
print(max(dp[-1]))
