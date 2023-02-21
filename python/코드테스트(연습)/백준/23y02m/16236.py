import sys

sys.stdin = open("16236.txt", "r")

from collections import deque

N = int(input())

sea = []
for i in range(N):
    data = list(map(int, input().split()))
    sea.append(data)

baby_shak = deque()
baby_shak.append(0)
baby_shak.append(0)


def bfs(y, x):
    return


for y in range(N):
    for x in range(N):
        if sea[y][x] == 9:
            bfs(y, x)
