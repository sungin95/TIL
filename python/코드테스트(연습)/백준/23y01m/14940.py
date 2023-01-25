import sys
from pprint import pprint

sys.stdin = open("14940.txt", "r")

from collections import deque

N, M = map(int, input().split())


map_ = []
for _ in range(N):
    data = list(map(int, input().split()))
    map_.append(data)

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def bfs(y, x, cnt):
    queue = deque()
    queue.append((y, x, cnt))
    while queue:
        cur = queue.popleft()
        for i in range(4):
            ny = cur[0] + dy[i]
            nx = cur[1] + dx[i]
            if 0 <= ny < N and 0 <= nx < M and map_[ny][nx] == 1:
                map_[ny][nx] = cur[2] + 1
                queue.append((ny, nx, cur[2] + 1))


for y in range(N):
    for x in range(M):
        if map_[y][x] == 2:
            map_[y][x] = 2
            bfs(y, x, 2)
            break

for y in range(N):
    for x in range(M):
        if map_[y][x] == 1:
            map_[y][x] = -1
        elif map_[y][x] == 0:
            pass
        else:
            map_[y][x] -= 2

for answer in map_:
    for a in answer:
        print(a, end=" ")
    else:
        print()
