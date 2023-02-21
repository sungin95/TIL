import sys

sys.stdin = open("2302.txt", "r")

N = int(input())
M = int(input())

vip = []
for _ in range(M):
    data = int(input()) + 1
    vip.append(data)
dp = [0 for i in range(N + 2)]
dp[0] = 0
dp[1] = 1
dp[2] = 1


def seat(n, vip):
    max_dp = 0
    if n == 1:
        return
    else:
        i = 1
        check = False
        while i <= n:
            i += 1
            if dp[i - 1] > max_dp:
                max_dp = dp[i - 1]

            if i not in vip:
                if check == False:
                    dp[i] = dp[i - 1] + dp[i - 2]
                else:
                    dp[i] = max_dp
                    check = False
            else:
                dp[i] = max_dp
                check = True


seat(N, vip)
print(max(dp))
