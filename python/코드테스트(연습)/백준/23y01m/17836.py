import sys

sys.stdin = open("17836.txt", "r")
from collections import deque

N, M, T = map(int, input().split())
# gram,y,x
visited = [[[False for i in range(M)] for i in range(N)] for i in range(2)]
castle = []
for y in range(N):
    data = input().split()
    castle.append(data)

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


def bfs(y, x, cnt):
    queue = deque()
    queue.append((y, x, cnt, 0))
    visited[0][y][x] = True

    while queue:
        y, x, cnt, gram = queue.popleft()
        if y == N - 1 and x == M - 1:
            print(cnt)
            break
        if cnt > T:
            continue
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if gram == 0:
                if 0 <= ny < N and 0 <= nx < M and visited[0][ny][nx] == False:
                    if castle[ny][nx] == "0":
                        queue.append((ny, nx, cnt + 1, 0))
                        visited[0][ny][nx] = True
                    elif castle[ny][nx] == "2":
                        queue.append((ny, nx, cnt + 1, 1))
                        visited[0][ny][nx] = True
            else:
                if 0 <= ny < N and 0 <= nx < M and visited[1][ny][nx] == False:
                    queue.append((ny, nx, cnt + 1, 1))
                    visited[1][ny][nx] = True
    else:
        print("Fail")


bfs(0, 0, 0)
