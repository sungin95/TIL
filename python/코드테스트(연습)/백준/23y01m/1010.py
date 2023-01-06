import sys

sys.stdin = open("1010.txt", "r")
import operator as op
from functools import reduce

# https://brownbears.tistory.com/459
def nCr(n, r):
    if n < 1 or r < 0 or n < r:
        raise ValueError
    r = min(r, n - r)
    numerator = reduce(op.mul, range(n, n - r, -1), 1)
    denominator = reduce(op.mul, range(1, r + 1), 1)
    return numerator // denominator


bridge = []
T = int(input())
answer_list = []
for i in range(T):
    N, M = map(int, input().split())
    cnt = 0
    str_ = "A" * M
    bridge.append(nCr(M, N))
for i in bridge:
    print(i)
