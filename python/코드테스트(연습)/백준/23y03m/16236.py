import sys
from heapq import heappop, heappush

sys.stdin = open("16236.txt", "r")

N = int(input())

sea = []
for i in range(N):
    data = list(map(int, input().split()))
    sea.append(data)

# 아기 상어는 처음 크기는 2이다.
baby_shak = list()
baby_shak.append("LEVEL UP")
baby_shak.append("LEVEL UP")
# 위 왼쪽 순
dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]


def bfs(y, x, eat_fish, time):
    if eat_fish == len(baby_shak):
        eat_fish = 0
        baby_shak.append("LEVEL UP")
    baby_shak_level = len(baby_shak)
    queue = []
    heappush(queue, (0, y, x))
    visited = [[False] * N for i in range(N)]
    visited[y][x] = True
    comparison = []
    while queue:
        cnt, y, x = heappop(queue)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == False:
                if comparison == []:
                    # 먹음
                    if sea[ny][nx] != 0 and sea[ny][nx] < baby_shak_level:
                        if comparison == []:
                            comparison.append((cnt + 1, ny, nx))
                    # 통과
                    elif sea[ny][nx] == 0 or sea[ny][nx] == baby_shak_level:
                        visited[ny][nx] = True
                        heappush(queue, (cnt + 1, ny, nx))
                # 물고기 1개 이상
                else:
                    if sea[ny][nx] != 0 and sea[ny][nx] < baby_shak_level:
                        if comparison[0][0] == (cnt + 1):
                            comparison.append((cnt + 1, ny, nx))

    else:
        if comparison == []:
            return
        # 마지막 탐색 대비
        else:
            comparison.sort()
            cnt, ny, nx = comparison[0]
            comparison = []
            time += cnt
            sea[ny][nx] = 0
            # print("좌표", ny, nx, "먹은 물고기", eat_fish + 1, time)  # 체크용
            answer[0] = time
            bfs(ny, nx, eat_fish + 1, time)


answer = [0]
for y in range(N):
    for x in range(N):
        if sea[y][x] == 9:
            sea[y][x] = 0
            bfs(y, x, 0, 0)
print(answer[0])
