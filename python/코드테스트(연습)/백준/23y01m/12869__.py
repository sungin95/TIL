import sys

sys.stdin = open("12869.txt", "r")

N = int(input())
scv = list(map(int, input().split()))
scv.append(0)
scv.append(0)
dp = [[[0] * 61 for i in range(61)] for i in range(61)]
dp[scv[0]][scv[1]][scv[2]] = 1
comb = [[9, 3, 1], [9, 1, 3], [3, 9, 1], [3, 1, 9], [1, 3, 9], [1, 9, 3]]
for i in range(60, -1, -1):
    for j in range(60, -1, -1):
        for k in range(60, -1, -1):
            if dp[i][j][k] > 0:
                for c in comb:
                    if i - c[0] >= 0:
                        i_ = i - c[0]
                    else:
                        i_ = 0
                    if j - c[1] >= 0:
                        j_ = j - c[1]
                    else:
                        j_ = 0
                    if k - c[2] >= 0:
                        k_ = k - c[2]
                    else:
                        k_ = 0
                    if dp[i_][j_][k_] == 0 or dp[i_][j_][k_] > dp[i][j][k] + 1:
                        dp[i_][j_][k_] = dp[i][j][k] + 1
print(dp[0][0][0] - 1)
