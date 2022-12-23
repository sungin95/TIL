# 답장을 너무 이상하게 보낸거 같아서 짜증나서 풀어 버렸다...

import sys

sys.stdin = open("2667.txt", "r")


N = int(input())
board = []
for _ in range(N):
    data = list(input())
    board.append(data)


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def make_complex(y, x, cnt):
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx and nx < N and 0 <= ny and ny < N and board[ny][nx] == "1":
            board[ny][nx] = str(pk)
            cnt[0] += 1
            make_complex(ny, nx, cnt)


pk = 2
cnt = [1]
cnt_list = []
for y in range(N):
    for x in range(N):
        if board[y][x] == "1":
            board[y][x] = str(pk)
            make_complex(y, x, cnt)
            pk += 1
            cnt_list.append(cnt[0])
            cnt = [1]

cnt_list.sort()
print(len(cnt_list))
for cnt_ in cnt_list:
    print(cnt_)
