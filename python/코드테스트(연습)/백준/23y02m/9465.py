import sys

sys.stdin = open("9465.txt", "r")

T = int(input())
answer_list = []
for _ in range(T):
    N = int(input())
    if N != 1:
        score = []
        for i in range(2):
            data = list(map(int, input().split()))
            score.append(data)
        dp = [[0] * N for i in range(2)]
        dp[0][0] = score[0][0]
        dp[1][0] = score[1][0]
        dp[0][1] = score[1][0] + score[0][1]
        dp[1][1] = score[0][0] + score[1][1]
        answer = 0
        for i in range(2, N):
            dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + score[0][i]
            dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + score[1][i]
        answer_list.append(max(dp[0][-1], dp[1][-1]))
    else:
        score = []
        for i in range(2):
            data = list(map(int, input().split()))
            score.append(data)
        answer_list.append(max(score[0][0], score[1][0]))


for a in answer_list:
    print(a)
