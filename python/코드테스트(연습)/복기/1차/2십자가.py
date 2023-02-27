# 가장 큰 십자가
import sys

sys.stdin = open("2.txt", "r")

# 십자가
cross = input().split()

# 각 선분을 dict을 통해 기록함. (dict.get()을 했을때 있으면 1, 없으면 None이 나오도록 )
cross_dict = {}
for x1, y1, x2, y2 in cross:
    if y1 == y2:
        y = int(y1)
        for x in range(int(x1), int(x2) + 1):
            if cross_dict.get((x, y)) == None:
                cross_dict[(x, y)] = 1
            else:
                cross_dict[(x, y)] += 1
    elif x1 == x2:
        x = int(x1)
        for y in range(int(y1), int(y2) + 1):
            if cross_dict.get((x, y)) == None:
                cross_dict[(x, y)] = 1
            else:
                cross_dict[(x, y)] += 1
# print(cross_dict)

# 교차되는 점을 찾기
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
cross_list = []
for kx, ky in cross_dict.keys():
    if cross_dict[(kx, ky)] >= 2:
        # print((kx, ky))
        for i in range(4):
            ny = ky + dy[i]
            nx = kx + dx[i]
            if cross_dict.get((nx, ny)) == None:
                break
        else:
            # print("cross", (kx, ky))
            # 교차되는 점을 찾는데 성공
            cross_list.append((kx, ky))

max_size = 0
for x, y in cross_list:
    # print("대각선", x, y)
    cnt = 0
    check = True
    while check:
        cnt += 1
        for i in range(4):
            ny = y + (dy[i] * cnt)
            nx = x + (dx[i] * cnt)
            # x축 방향을 이동할 때
            if dy[i] == 0:
                # print(nx, ny)
                if (
                    cross_dict.get((nx, ny + 1)) != None
                    or cross_dict.get((nx, ny - 1)) != None
                ):
                    # print(nx, ny)
                    check = False
                    break
            # y축 방향을 이동할 때
            if dx[i] == 0:
                # print(nx, ny)
                if (
                    cross_dict.get((nx + 1, ny)) != None
                    or cross_dict.get((nx - 1, ny)) != None
                ):
                    # print(nx, ny)
                    check = False
                    break
            # 점
            if cross_dict.get((nx, ny)) == None:
                check = False
                # print(nx, ny)
                break
        else:
            # print(x, y, cnt)
            if max_size < cnt:
                max_size = cnt

print(max_size)

# 문제점: 점을 기준으로 했는데.(3,3)(x,y) 선분으로 표현을 해야 더 정확했을거 같다 (3,3,4,3)(x1,y1,x2,y2)
