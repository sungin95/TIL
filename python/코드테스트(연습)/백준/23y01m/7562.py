from pprint import pprint

from collections import deque

T = int(input())

dy = [-2, -2, -1, -1, 1, 1, 2, 2]
dx = [-1, 1, -2, 2, -2, 2, -1, 1]

answer_list = []
for t in range(T):
    N = int(input())
    board = [[0 for i in range(N)] for i in range(N)]
    queue = deque()
    start_y, start_x = map(int, input().split())
    end_y, end_x = map(int, input().split())
    queue.append((start_y, start_x, 1))
    board[start_y][start_x] = 1
    while queue:
        cur = queue.popleft()
        if cur[0] == end_y and cur[1] == end_x:
            answer_list.append(cur[2])
            break
        for i in range(8):
            ny = cur[0] + dy[i]
            nx = cur[1] + dx[i]
            if 0 <= ny < N and 0 <= nx < N and board[ny][nx] == 0:
                queue.append((ny, nx, cur[2] + 1))
                board[ny][nx] = cur[2]
for answer in answer_list:
    print(answer - 1)
