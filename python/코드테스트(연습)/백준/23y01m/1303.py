import sys

sys.stdin = open("1303.txt", "r")

N, M = map(int, input().split())

war_field = []
for i in range(M):
    data = list(input())
    war_field.append(data)
visited = [[False for i in range(N)] for i in range(M)]
white = 0
blue = 0

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def group(y, x):
    global white
    global blue
    affiliation = war_field[y][x]
    stack = [(y, x)]
    visited[y][x] = True
    cnt = 1
    while stack:
        cur = stack.pop()
        for i in range(4):
            ny = cur[0] + dy[i]
            nx = cur[1] + dx[i]
            if (
                0 <= ny < M
                and 0 <= nx < N
                and visited[ny][nx] == False
                and war_field[ny][nx] == affiliation
            ):
                cnt += 1
                visited[ny][nx] = True
                stack.append((ny, nx))
    if affiliation == "W":
        white += cnt**2
    else:
        blue += cnt**2


for y in range(M):
    for x in range(N):
        if visited[y][x] == False:
            group(y, x)
print(white, blue)
