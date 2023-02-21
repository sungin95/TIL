import sys

sys.stdin = open("3190.txt", "r")

from collections import deque

N = int(input())
Map_ = [["X"] * N for i in range(N)]
Apple = int(input())
for i in range(Apple):
    y, x = map(int, input().split())
    Map_[y - 1][x - 1] = "a"
d = int(input())
direct = deque()
for i in range(d):
    t, di = input().split()
    direct.append((int(t) + 1, di))

# 오른쪽은 +1, 왼쪽은 -1
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
# 몸통, 사과를 안 먹으면 popleft
body = deque()
# y, x
body.append((0, 0))
dire = 0
time = 0

try:
    while True:
        time += 1
        if direct and direct[0][0] == time:
            t, di = direct.popleft()
            if di == "D":
                dire += 1
            elif di == "L":
                dire -= 1
            if 0 > dire:
                dire += 4
            if dire <= 4:
                dire = dire % 4

        y, x = body[-1]
        ny = y + dy[dire]
        nx = x + dx[dire]
        # print(time, ny, nx, body, dire)
        if 0 <= ny < N and 0 <= nx < N and (ny, nx) not in body:
            if Map_[ny][nx] == "X":
                body.append((ny, nx))
                body.popleft()
            elif Map_[ny][nx] == "a":
                Map_[ny][nx] = "X"
                body.append((ny, nx))
        else:
            raise
except:
    print(time)
