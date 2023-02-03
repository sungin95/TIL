import sys

sys.stdin = open("14501.txt", "r")

from collections import deque

N = int(input())

max_dp = [0] * N
counseling = []
for i in range(N):
    c, b = map(int, input().split())
    counseling.append((i, c, b))
stack = deque()
stack.append((0, 0))
while stack:
    i, b = stack.popleft()
    try:
        if max_dp[i] <= b:
            max_dp[i] = b

        if counseling[i][1] + i < N + 1:
            if max_dp[i] < b + counseling[i][2]:
                max_dp[i] = b + counseling[i][2]
                stack.append((counseling[i][1] + i, b + counseling[i][2]))

        if i + 1 < N + 1:
            stack.append((i + 1, b))
    except:
        pass
print(max(max_dp))
