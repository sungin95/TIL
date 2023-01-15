# DP의 핵심은 DP는 언제나 최소 or 최대값등 내가 원하는 값을 저장해 놓은 상태이고
# 이전 DP들의 값의 의미를 파악해서 그 값과 비교해서 다음 값을 찾아나가는 과정이 아닐까 싶다.
import sys

sys.stdin = open("1699.txt", "r")

N = int(input())

DP = [i for i in range(N + 1)]

for i in range(N + 1):
    for j in range(i + 1):
        if j * j > i:
            break
        else:
            if DP[i] > DP[i - (j * j)] + 1:
                DP[i] = DP[i - (j * j)] + 1

print(DP[-1])
