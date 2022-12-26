import sys

sys.stdin = open("1987.txt", "r")

N, M = map(int, input().split())

board = []
check_board = []
for _ in range(N):
    data = list(input())
    board.append(data)
for a in range(N):
    check_board.append([])
    for b in range(M):
        check_board[-1].append(dict())
alph = set()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def move(y, x, max_cnt):
    passage = board[y][x]
    alph.add(passage)
    # print(check_board)
    # print(check_board[y][x][0])
    # print(type(check_board[y][x]))
    # print(str(alph))
    if check_board[y][x].get(str(alph)) is not None:
        alph.remove(passage)
        return
    else:
        check_board[y][x][str(alph)] = alph

    if max_cnt[0] < len(alph):
        max_cnt[0] = len(alph)
        if max_cnt[0] == 26:
            return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < M and 0 <= ny and ny < N and board[ny][nx] not in alph:
            move(ny, nx, max_cnt)
    else:
        alph.remove(passage)


max_cnt = [0]
move(0, 0, max_cnt)
print(max_cnt[0])
# print(check_board)
