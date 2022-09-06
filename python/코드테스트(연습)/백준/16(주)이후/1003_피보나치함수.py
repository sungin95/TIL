import sys
sys.stdin = open("1003.txt", "r")
answer_list = []
n = int(input())
for i in range(n):
    m = int(input())
    dp = []
    for i in range(m+1):
        if i == 0:
            dp.append([1,0])
        elif i == 1:
            dp.append([0,1])
        else:
            a = 0
            b = 0
            a = dp[i-1][0] + dp[i-2][0]
            b = dp[i-1][1] + dp[i-2][1]
            dp.append([a,b])
    answer_list.append(dp[-1])
for ans in answer_list:
    print(ans[0], ans[1])