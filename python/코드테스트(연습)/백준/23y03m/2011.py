num = list(input())

num_dict = {}
for i in range(1, 27):
    num_dict[str(i)] = 1

dp = [0] * (len(num) + 1)
dp[0] = 1
dp[1] = 1
# 왜 계속 틀리나 했더니 맨 앞자리 0....
if num[0] == "0":
    print("0")
else:
    for i in range(2, len(num) + 1):
        if num[i - 1] != "0":
            dp[i] += (dp[i - 1]) % 1000000
        if num_dict.get(num[i - 2] + num[i - 1]) == 1:
            dp[i] += dp[i - 2] % 1000000

    else:
        print(dp[-1] % 1000000)
