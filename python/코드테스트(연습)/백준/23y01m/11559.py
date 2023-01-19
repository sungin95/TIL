from pprint import pprint
import sys

sys.stdin = open("11559.txt", "r")

N = 12
M = 6
puyo_puyo = []
for i in range(12):
    data = list(input())
    puyo_puyo.append(data)

visited = [[False for i in range(6)] for i in range(12)]
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

save_stack = []


def boom(y, x):
    # 왜 visited이건 글로벌을 줘야 하지?
    global visited
    global save_stack
    cnt = 1
    RGBPY = puyo_puyo[y][x]
    stack = [(y, x)]
    save_stack.append([])
    save_stack[-1].append((y, x))
    while stack:
        cur = stack.pop()
        for i in range(4):
            ny = cur[0] + dy[i]
            nx = cur[1] + dx[i]
            if (
                0 <= ny < 12
                and 0 <= nx < 6
                and puyo_puyo[ny][nx] == RGBPY
                and visited[ny][nx] == False
            ):
                cnt += 1
                visited[ny][nx] = True
                stack.append((ny, nx))
                save_stack[-1].append((ny, nx))
    if cnt < 4:
        save_stack.pop()


def reset():
    global visited
    global save_stack
    global stop
    if save_stack:
        answer[0] += 1
    else:
        stop = False
    visited = [[False for i in range(6)] for i in range(12)]
    for save in save_stack:
        for ss in save:
            puyo_puyo[ss[0]][ss[1]] = "."
    for x in range(6):
        text = ""
        for y in range(11, -1, -1):
            if puyo_puyo[y][x] != ".":
                text += puyo_puyo[y][x]
        else:
            for y in range(11, -1, -1):
                try:
                    puyo_puyo[y][x] = text[11 - y]
                except:
                    puyo_puyo[y][x] = "."
    save_stack = []


answer = [0]
stop = True
while stop:
    for y in range(11, -1, -1):
        for x in range(5, -1, -1):
            if puyo_puyo[y][x] != "." and visited[y][x] == False:
                visited[y][x] = True
                boom(y, x)
    reset()
print(answer[0])
