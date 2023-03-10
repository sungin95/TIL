import sys

sys.stdin = open("14003.txt", "r")

N = int(input())
num = list(map(int, input().split()))
dp = [1] * N
dp[0] = 1
for i in range(1, N):
    for j in range(i):
        if num[j] < num[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
max_dp = max(dp)
max_index = dp.index(max(dp))

answer = []
for i in range(max_index, -1, -1):
    if dp[i] == max_dp:
        answer.append(num[i])
        max_dp -= 1
answer.reverse()
print(*answer)
