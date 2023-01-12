import sys

sys.stdin = open("1912.txt", "r")

N = int(input())

num_list = list(map(int, input().split()))

dp = [0] * N

sum_ = 0
for i in range(N):
    sum_ += num_list[i]
    if sum_ < 0:
        sum_ = 0
    dp[i] = sum_
max_ = max(dp)
if max_ == 0:
    print(max(num_list))
else:
    print(max_)
