from collections import deque
import sys
sys.stdin = open("7576.txt", 'r')

n, m = map(int, input().split())
board = []
for _ in range(m):
    data = list(map(int, input().split()))
    board.append(data)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()


for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            queue.append([i, j])
print(queue)
while queue:
    A = queue.popleft()
    for i in range(4):
        nx = A[0] + dx[i]
        ny = A[1] + dy[i]
        if 0 <= nx and nx < m and 0 <= ny and ny < n:
            if board[nx][ny] == 0:
                board[nx][ny] = 1
                queue.append([nx, ny])
print(board)
for i in range(m):
    if 0 in board[i]:
        print(-1)
        break
else:
    print(1)
