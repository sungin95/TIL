import sys

sys.stdin = open("6593.txt", "r")
from collections import deque

from pprint import pprint

answer_list = []
while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break
    buliding = []
    S_E = {}
    for l in range(L):
        buliding.append([])
        for r in range(R + 1):
            data = list(input())
            if data:
                buliding[-1].append(data)
                for c in range(len(data)):
                    if data[c] == "S":
                        S_E["S"] = (l, r, c, 0)
                    if data[c] == "E":
                        S_E["E"] = (l, r, c)
    # print(S_E)

    dy = [0, 0, 0, 0, 1, -1]
    dx = [0, 0, 1, -1, 0, 0]
    dz = [1, -1, 0, 0, 0, 0]

    queue = deque()
    queue.append(S_E["S"])
    ans_check = False
    while queue:
        l, r, c, t = queue.popleft()
        for i in range(6):
            ny = r + dy[i]
            nx = c + dx[i]
            nz = l + dz[i]
            if 0 <= ny < R and 0 <= nx < C and 0 <= nz < L:
                if buliding[nz][ny][nx] == ".":
                    queue.append((nz, ny, nx, t + 1))
                    buliding[nz][ny][nx] = "#"
                elif buliding[nz][ny][nx] == "E":
                    answer_list.append(f"Escaped in {t+1} minute(s).")
                    ans_check = True
                    queue = []

    else:
        if ans_check == False:
            answer_list.append("Trapped!")

for a in answer_list:
    print(a)
