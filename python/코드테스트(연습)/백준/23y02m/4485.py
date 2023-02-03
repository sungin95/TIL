import sys

# sys.stdin = open("4485.txt", "r")
INF = sys.maxsize
from heapq import heappop, heappush

answer_list = []
while True:
    N = int(input())
    if not N:
        break
    cave = []
    for _ in range(N):
        data = list(map(int, input().split()))
        cave.append(data)
    visited = [[INF] * N for i in range(N)]

    start = []
    heappush(start, (cave[0][0], 0, 0))
    visited[0][0] = cave[0][0]

    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]

    while start:
        cost, y, x = heappop(start)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if visited[ny][nx] > cost + cave[ny][nx]:
                    visited[ny][nx] = cost + cave[ny][nx]
                    heappush(start, (cost + cave[ny][nx], ny, nx))
    answer_list.append(visited[-1][-1])
for i in range(1, len(answer_list) + 1):
    print(f"Problem {i}:", answer_list[i - 1])
