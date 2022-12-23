# 뭐지... python은 안되고, PyPy3는 되고...

import sys
from pprint import pprint

sys.stdin = open("1012.txt", "r")

T = int(input())
for t in range(T):
    board = []
    N, M, K = map(int, input().split())

    for i in range(N):
        board.append([])
        for j in range(M):
            board[-1].append("0")

    for _ in range(K):
        y, x = map(int, input().split())
        board[y][x] = "1"

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def cabbages(y, x):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx < M and 0 <= ny and ny < N and board[ny][nx] == "1":
                board[ny][nx] = "2"
                cabbages(ny, nx)

    cnt = 0
    for y in range(N):
        for x in range(M):
            if board[y][x] == "1":
                board[y][x] = "2"
                cabbages(y, x)
                cnt += 1
    # pprint(board)
    print(cnt)
