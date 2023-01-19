import sys

sys.stdin = open("5014.txt", "r")
from collections import deque

queue = deque()
F, start, goal, up, down = map(int, input().split())

floor = [0 for i in range(F + 1)]
queue.append((start, 0))
floor[start] = "start"
check = False
while queue:
    cur = queue.popleft()
    if cur[0] == goal:
        print(cur[1])
        # print(floor)
        check = True
        break
    # 코드 리뷰 해 보니까 여기를 for문으로 합쳐 줄 수 있었다.
    nu = cur[0] + up
    if 0 < nu <= F and floor[nu] == 0:
        floor[nu] = cur[1] + 1
        queue.append((nu, cur[1] + 1))
    nd = cur[0] - down
    if 0 < nd <= F and floor[nd] == 0:
        floor[nd] = cur[1] + 1
        queue.append((nd, cur[1] + 1))
if check == False:
    print("use the stairs")
