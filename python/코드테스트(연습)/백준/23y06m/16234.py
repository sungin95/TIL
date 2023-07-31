import sys

sys.stdin = open("16234.txt", "r")
import sys

input = sys.stdin.readline
from collections import deque

graph = []
n, l, r = map(int, input().split())
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(a, b):
    q = deque()
    temp = []
    q.append((a, b))
    temp.append((a, b))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    temp.append((nx, ny))
                    visited[nx][ny] = 1
    return temp


result = 0
while 1:
    flag = 0
    visited = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                # y,x를 같게 했더니 혼선이 있었나보다... 주의해야 겠다.
                country = bfs(i, j)
                if len(country) > 1:
                    flag = 1
                    number = sum([graph[x][y] for x, y in country]) // len(country)

                    for y, x in country:
                        graph[y][x] = number
    if flag == 0:
        break
    result += 1

print(result)
