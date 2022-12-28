import sys

sys.stdin = open("2630.txt", "r")

N = int(input())
board = []
for i in range(N):
    data = input().split()
    board.append(data)

cnt = [0, 0]


def half(sy, ey, sx, ex):
    white_check = set()
    blue_check = set()
    for y in range(sy, ey):
        for x in range(sx, ex):
            if board[y][x] == "1":
                blue_check.add("check")
            else:
                white_check.add("check")

            if blue_check & white_check == {"check"}:
                my = (ey + sy) // 2
                mx = (ex + sx) // 2
                half(sy, my, sx, mx)
                half(my, ey, sx, mx)
                half(sy, my, mx, ex)
                half(my, ey, mx, ex)
                return
    else:

        if white_check == set():
            cnt[1] += 1
            # print(sy, ey, sx, ex, "blue")
        else:
            cnt[0] += 1
            # print(sy, ey, sx, ex, "white")


half(0, N, 0, N)
print(cnt[0])
print(cnt[1])
# 0123 4567
