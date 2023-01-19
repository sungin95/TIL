import sys

sys.stdin = open("10026.txt", "r")
from pprint import pprint

N = int(input())
map_ = []
for i in range(N):
    data = list(input())
    map_.append(data)


visited = [[[False for i in range(N)] for i in range(N)] for i in range(2)]


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
cnt = [0, 0]


def RGB(y, x):
    cnt[0] += 1
    rgb = map_[y][x]
    visited[0][y][x] = True
    stack = [(y, x)]
    while stack:
        cur = stack.pop()
        for i in range(4):
            ny = cur[0] + dy[i]
            nx = cur[1] + dx[i]
            if (
                0 <= ny < N
                and 0 <= nx < N
                and map_[ny][nx] == rgb
                and visited[0][ny][nx] == False
            ):
                visited[0][ny][nx] = True
                stack.append((ny, nx))


def R_GB(y, x):
    cnt[1] += 1
    if map_[y][x] == "R" or map_[y][x] == "G":
        rgb = ["R", "G"]
    else:
        rgb = ["B"]
    visited[1][y][x] = True
    stack = [(y, x)]
    while stack:
        cur = stack.pop()
        for i in range(4):
            ny = cur[0] + dy[i]
            nx = cur[1] + dx[i]
            if (
                0 <= ny < N
                and 0 <= nx < N
                and map_[ny][nx] in rgb
                and visited[1][ny][nx] == False
            ):
                visited[1][ny][nx] = True
                stack.append((ny, nx))


for y in range(N):
    for x in range(N):
        if visited[0][y][x] == False:
            RGB(y, x)
        if visited[1][y][x] == False:
            R_GB(y, x)

print(cnt[0], cnt[1])
