import sys

sys.stdin = open("12015.txt", "r")
# 12015번
import sys
from bisect import bisect_left

input = sys.stdin.readline
while True:
    N = input()
    arr = list(map(int, input().split()))
    if not N:
        break
    N = int(N)
    dp = [arr[0]]

    for i in range(N):
        if arr[i] > dp[-1]:
            dp.append(arr[i])
        else:
            idx = bisect_left(dp, arr[i])
            dp[idx] = arr[i]
    print(len(dp))

# 구글링을 통해 해결을 하였고
# 결국 이 문제의 핵심은 최대 값을 구하는 것이었고
# 이때 그 값들을 dp에다가 저장을 한다.
# 그리고 최대 값이 아니면
# 찾은 값중을 순서에 맞게 넣어주면 최대 갯수가 유지가 되면서
# dp값들이 변하게 된다.
# 결국 dp의 길이가 답이 된다.
