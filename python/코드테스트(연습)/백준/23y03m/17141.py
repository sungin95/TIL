import sys

sys.stdin = open("17141.txt", "r")
from itertools import combinations
from collections import deque

INF = sys.maxsize
N, M = map(int, input().split())

gragh = []
for i in range(N):
    data = input().split()
    gragh.append(data)


queue = deque()
for y in range(N):
    for x in range(N):
        if gragh[y][x] == "2":
            queue.append((y, x, 0))

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

c_queue = combinations(queue, M)
min_time = INF
for queue_three in c_queue:
    queue = deque(queue_three)
    visited = [[False] * N for i in range(N)]
    # print(queue)
    for y, x, _ in queue:
        visited[y][x] = True
    while queue:
        y, x, t = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (
                0 <= ny < N
                and 0 <= nx < N
                and visited[ny][nx] == False
                and gragh[ny][nx] != "1"
            ):
                gragh[ny][nx] = "2"
                visited[ny][nx] = True
                queue.append((ny, nx, t + 1))
    else:
        check = False
        for i in range(N):
            if check == True:
                break
            for j in range(N):
                if visited[i][j] != True and gragh[i][j] != "1":
                    check = True
                    break
        else:
            if min_time > t:
                min_time = t

if min_time == INF:
    print(-1)
else:
    print(min_time)
