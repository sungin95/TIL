# 아직
import sys

sys.stdin = open("14003.txt", "r")

from bisect import bisect_left

N = int(input())
arr = list(map(int, input().split()))

dp = [arr[0]]

for i in range(N):
    # print((dp))
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        idx = bisect_left(dp, arr[i])
        dp[idx] = arr[i]
print(len(dp))
print(*dp)
