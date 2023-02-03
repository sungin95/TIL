import sys

sys.stdin = open("1261.txt", "r")
from heapq import heappop, heappush


N, M = map(int, input().split())

miro = []
for _ in range(M):
    data = list(input())
    miro.append(data)

start = [(0, 0, 0)]
visited = [[False] * N for i in range(M)]
visited[0][0] = True
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

while start:
    cnt, y, x = heappop(start)
    if (y, x) == (M - 1, N - 1):
        print(cnt)
        break
    for i in range(4):
        (ny, nx) = (y + dy[i], x + dx[i])
        if 0 <= ny < M and 0 <= nx < N and visited[ny][nx] == False:
            visited[ny][nx] = True
            if miro[ny][nx] == "1":
                heappush(start, (cnt + 1, ny, nx))
            else:
                heappush(start, (cnt, ny, nx))
