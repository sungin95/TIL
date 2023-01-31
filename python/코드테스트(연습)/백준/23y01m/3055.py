import sys

sys.stdin = open("3055.txt", "r")

from collections import deque

R, S = map(int, input().split())

map_ = []
for i in range(R):
    data = list(input())
    map_.append(data)

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
visited = [[False for i in range(S)] for i in range(R)]

DorWater = []
for y in range(R):
    for x in range(S):
        if map_[y][x] == "*" or map_[y][x] == "S":
            DorWater.append((map_[y][x], y, x, 0))
            visited[y][x]
DorWater.sort()

queue = deque()
for d in DorWater:
    queue.append(d)


answer = []
while queue:
    dw, y, x, cnt = queue.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if (
            0 <= ny < R
            and 0 <= nx < S
            and visited[ny][nx] == False
            and map_[ny][nx] != "X"
        ):
            if map_[ny][nx] == ".":
                map_[ny][nx] = dw
                visited[ny][nx] = True
                queue.append((dw, ny, nx, cnt + 1))
            elif map_[ny][nx] == "D" and dw == "S":
                answer.append(cnt + 1)
                queue = []
                break
if answer:
    print(answer[0])
else:
    print("KAKTUS")
