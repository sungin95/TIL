import sys
from pprint import pprint

sys.stdin = open("2206.txt", "r")


import copy

N, M = map(int, input().split())

map_ = []
for i in range(N):
    data = list(input())
    map_.append(data)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

cnt_ = [10000000]

map_dict = {}
map_dict_check = {}


def move(y, x, check, cnt, map_):
    global N
    global M
    if y == (N - 1) and x == (M - 1):
        if cnt_[0] > cnt:
            cnt_[0] = cnt
        return
    if cnt_[0] < cnt:
        return
    cnt += 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < M:
            if map_[ny][nx] == "1" and check == False:
                map_[ny][nx] = "2"
                check = True
                if map_dict_check.get((ny, nx)) == None:
                    map_dict_check[(ny, nx)] = cnt
                    move(ny, nx, check, cnt, map_)
                else:
                    if map_dict_check[(ny, nx)] >= cnt:
                        map_dict_check[(ny, nx)] = cnt
                        move(ny, nx, check, cnt, map_)
                map_[ny][nx] = "1"
                check = False

            elif map_[ny][nx] == "0":
                map_[ny][nx] = "2"
                if check == False:
                    if map_dict.get((ny, nx)) == None:
                        map_dict[(ny, nx)] = cnt
                        if map_dict_check.get((ny, nx)) == None:
                            map_dict_check[(ny, nx)] = cnt
                        else:
                            if map_dict_check[(ny, nx)] > cnt:
                                map_dict_check[(ny, nx)] = cnt
                        move(ny, nx, check, cnt, map_)

                    else:
                        if map_dict[(ny, nx)] >= cnt:
                            map_dict[(ny, nx)] = cnt
                            if map_dict_check[(ny, nx)] > cnt:
                                map_dict_check[(ny, nx)] = cnt
                            move(ny, nx, check, cnt, map_)
                else:
                    if map_dict_check.get((ny, nx)) == None:
                        map_dict_check[(ny, nx)] = cnt
                        move(ny, nx, check, cnt, map_)

                    else:
                        if map_dict_check[(ny, nx)] >= cnt:
                            map_dict_check[(ny, nx)] = cnt
                            move(ny, nx, check, cnt, map_)
                map_[ny][nx] = "0"


check = False
map_[0][0] = "2"
map_dict[(0, 0)] = 1
map_dict_check[(0, 0)] = 1
move(0, 0, check, 1, map_)
if cnt_[0] == 10000000:
    print(-1)
else:
    # print(map_dict)
    # print(map_dict_check)
    print(cnt_[0])
