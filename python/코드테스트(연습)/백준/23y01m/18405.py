import sys

sys.stdin = open("18405.txt", "r")
from pprint import pprint

from collections import deque

N, M = map(int, input().split())

map_ = []
for i in range(N):
    data = list(map(int, input().split()))
    map_.append(data)
S, Y, X = map(int, input().split())

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

start = (Y - 1, X - 1, 1)
queue = deque()
queue.append(start)
answer = []
finsh = -1
while queue:
    cur = queue.popleft()
    if finsh == -1 or finsh == cur[2]:
        for i in range(4):
            ny = cur[0] + dy[i]
            nx = cur[1] + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if map_[ny][nx] == 0:
                    queue.append((ny, nx, cur[2] + 1))
                else:
                    answer.append((map_[ny][nx], cur[2]))
                    finsh = cur[2]
ans = min(answer)
if ans[1] > S:
    print(0)
else:
    print(ans[0])
