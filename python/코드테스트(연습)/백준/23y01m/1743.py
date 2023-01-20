from pprint import pprint

N, M, K = map(int, input().split())

hallway = []
for y in range(N):
    hallway.append([])
    for x in range(M):
        hallway[-1].append(".")
for i in range(K):
    y, x = map(int, input().split())
    hallway[y - 1][x - 1] = "#"

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

max_cnt = [1]


def big_garbage(y, x):
    global max_cnt
    cnt = 1
    hallway[y][x] = "."
    stack = [(y, x)]
    while stack:
        cur = stack.pop()
        for i in range(4):
            ny = cur[0] + dy[i]
            nx = cur[1] + dx[i]
            if 0 <= ny < N and 0 <= nx < M and hallway[ny][nx] == "#":
                cnt += 1
                hallway[ny][nx] = "."
                stack.append((ny, nx))
                if max_cnt[0] < cnt:
                    max_cnt[0] = cnt


for y in range(N):
    for x in range(M):
        if hallway[y][x] == "#":
            big_garbage(y, x)

print(max_cnt[0])
