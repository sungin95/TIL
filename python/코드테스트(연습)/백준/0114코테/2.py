import sys
from pprint import pprint

sys.stdin = open("2.txt", "r")

N, M = map(int, input().split())

map_ = []
for _ in range(N):
    data = list(map(int, input().split()))
    map_.append(data)

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def same_area(y, x):
    global N
    global M
    stack = [[y, x]]
    while stack:
        aaa = stack.pop()
        for i in range(4):
            ny = aaa[0] + dy[i]
            nx = aaa[1] + dx[i]
            if ny < 0:
                ny = N + ny
            elif N <= ny:
                ny -= N
            elif nx < 0:
                nx = M + nx
            elif M <= nx:
                nx -= M

            if map_[ny][nx] == 0:
                map_[ny][nx] = 1
                stack.append([ny, nx])


cnt = [0]
for y in range(N):
    for x in range(M):
        if map_[y][x] == 0:
            map_[y][x] = 1
            same_area(y, x)
            cnt[0] += 1


print(cnt[0])
