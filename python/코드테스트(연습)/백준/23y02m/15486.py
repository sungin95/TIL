import sys

sys.stdin = open("14501.txt", "r")

N = int(input())
# dp를 현재까지 최대값에 새롭게 더해 줄래? 아니면 바뀌는 값을 사용 할래 문제였다.
max_dp = [0] * (N + 1)
counseling = []
for i in range(N):
    c, b = map(int, input().split())
    counseling.append((c, b))
M = 0
for i in range(N):
    M = max(M, max_dp[i])
    if i + counseling[i][0] > N:
        continue
    max_dp[i + counseling[i][0]] = max(
        max_dp[i + counseling[i][0]], M + counseling[i][1]
    )
print(max(max_dp))
