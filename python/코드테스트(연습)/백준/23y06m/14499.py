import sys

sys.stdin = open("14499.txt", "r")

N, M, x, y, K = map(int, input().split())
map_ = []
for _ in range(N):
    map_.append(list(map(int, input().split())))
command = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0]
direction_list = [
    [],
    [4, 3, 1, 2, 5, 6],
    [3, 4, 2, 1, 5, 6],
    [5, 6, 3, 4, 2, 1],
    [6, 5, 3, 4, 1, 2],
]


def move(s_x, s_y, direction):
    new_dice = [0, 0, 0, 0, 0, 0]
    for i in range(6):
        new_dice[i] = dice[direction_list[direction][i] - 1]
    if map_[s_y][s_x] == 0:
        map_[s_y][s_x] = new_dice[1]
    else:
        new_dice[1] = map_[s_y][s_x]
        map_[s_y][s_x] = 0
    print(new_dice[0])

    return new_dice


dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]

for k in command:
    nx = x + dr[k]
    ny = y + dc[k]
    if 0 <= nx < N and 0 <= ny < M:
        dice = move(ny, nx, k)
        x, y = nx, ny


# , new_dice[5], new_dice[2], new_dice[3], new_dice[4], new_dice[1])
