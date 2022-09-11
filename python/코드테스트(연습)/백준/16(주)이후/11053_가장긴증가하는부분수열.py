import sys
sys.stdin = open("11053.txt", "r")

t = int(input())
arr = list(map(int, input().split()))
dp = [1 for i in range(t)]
for i in range(t):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
