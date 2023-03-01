N = int(input())
card_pay = list(map(int, input().split()))
dp = [0] * (N + 1)


for i in range(1, N + 1):
    for j in range(i, N + 1):
        dp[j] = max(dp[j - i] + card_pay[i - 1], dp[j])
print(dp[-1])
