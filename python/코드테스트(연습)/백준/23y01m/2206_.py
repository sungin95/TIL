import sys
from pprint import pprint

sys.stdin = open("2206.txt", "r")

from collections import deque

N, M = map(int, input().split())

map_ = []
for i in range(N):
    data = list(map(int, input()))
    map_.append(data)

viseted = [[[False for i in range(M)] for j in range(N)] for k in range(2)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

start = (0, 0, 0, 1)
queue = deque()
queue.append(start)
viseted[0][0][0] = True
cnt = 1
min_cnt = 10000000
while queue:
    cur = queue.popleft()
    if cur[0] == N - 1 and cur[1] == M - 1:
        if min_cnt > cur[3]:
            min_cnt = cur[3]
            print(min_cnt)
            break
    for i in range(4):
        ny = cur[0] + dy[i]
        nx = cur[1] + dx[i]
        if 0 <= ny < N and 0 <= nx < M:
            if cur[2] == 0:
                if map_[ny][nx] == 0 and viseted[0][ny][nx] == False:
                    viseted[0][ny][nx] = True
                    viseted[1][ny][nx] = True
                    queue.append((ny, nx, 0, cur[3] + 1))
                elif map_[ny][nx] == 1 and viseted[0][ny][nx] == False:
                    viseted[0][ny][nx] = True
                    viseted[1][ny][nx] = True
                    queue.append((ny, nx, 1, cur[3] + 1))
            elif cur[2] == 1 and map_[ny][nx] == 0 and viseted[1][ny][nx] == False:
                viseted[1][ny][nx] = True
                queue.append((ny, nx, 1, cur[3] + 1))
if min_cnt == 10000000:
    print(-1)
