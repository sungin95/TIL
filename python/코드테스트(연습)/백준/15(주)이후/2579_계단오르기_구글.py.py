import sys
sys.stdin = open("2579.txt", "r")

n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

dp = [0]*n

if n == 1:
    print(array[0])
elif n == 2:
    print(array[0] + array[1])    

else:
    dp[0] = array[0]
    dp[1] = max(array[0]+array[1], array[1])
    dp[2] = max(array[0]+array[2], array[1]+array[2])

    for i in range(3, n):
        dp[i] = max(array[i]+dp[i-2], array[i]+array[i-1]+dp[i-3])

    print(dp[n-1])