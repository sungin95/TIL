import sys
from pprint import pprint

sys.stdin = open("5427.txt", "r")

from collections import deque

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
answer_list = []
T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    building = []
    for i in range(M):
        data = list(input())
        building.append(data)
    queue = deque()
    for y in range(M):
        for x in range(N):
            if building[y][x] == "*":
                queue.append(("*", y, x))
            elif building[y][x] == "@":
                start = ("@", y, x, 0)
    else:
        queue.append(start)
    check = False
    while queue:
        cur = queue.popleft()
        for i in range(4):
            if check == False:
                ny = cur[1] + dy[i]
                nx = cur[2] + dx[i]
                # 불일때
                if cur[0] == "*":
                    if 0 <= ny < M and 0 <= nx < N and building[ny][nx] == ".":
                        building[ny][nx] = "*"
                        queue.append(("*", ny, nx))
                # 사람
                else:
                    if 0 <= ny < M and 0 <= nx < N:
                        if building[ny][nx] == ".":
                            building[ny][nx] = "@"
                            queue.append(("@", ny, nx, cur[3] + 1))
                    else:
                        answer_list.append(cur[3] + 1)
                        # while 문 멈출겸 틀리면 오류를 내기 위해 덱을 빈 리스트 형태로 저장
                        queue = []
                        check = True

    if check == False:
        answer_list.append("IMPOSSIBLE")

for answer in answer_list:
    print(answer)
