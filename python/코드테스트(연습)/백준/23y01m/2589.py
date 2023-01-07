import sys
from pprint import pprint

sys.stdin = open("2589.txt", "r")

from collections import deque

N, M = map(int, input().split())
map_ = []
for i in range(N):
    data = list(input())
    map_.append(data)

# pprint(map_)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

max_ = [0]


def check_L(y, x):
    if map_[y][x] == "W":
        return
    elif map_[y][x] == "L":
        L = "L"
        K = "K"
    elif map_[y][x] == "K":
        L = "K"
        K = "L"
    queue = deque()

    queue.append((y, x, 0))
    map_[y][x] = K
    while queue:
        cur = queue.popleft()
        cnt = cur[2]

        for i in range(4):
            ny = cur[0] + dy[i]
            nx = cur[1] + dx[i]
            if 0 <= ny < N and 0 <= nx < M and map_[ny][nx] == L:
                queue.append((ny, nx, cnt + 1))
                map_[ny][nx] = K
                if max_[0] < cnt + 1:
                    max_[0] = cnt + 1


for y in range(N):
    for x in range(M):
        check_L(y, x)
print(max_[0])
# 애먹었던 점
# cnt플1을 하는 시점에 K를 붙여야 했는데 그렇게 안해서 불필요한 계산 과정이 많아 졌다.
