from collections import deque
from copy import copy
import sys
sys.stdin = open("7569.txt", 'r')
"""
델타 탐색과 큐 구조의 bfs를 이용하여 익은 토마토 모두 체크
여기서 날짜를 구해 줘야 해서 하루치 작업을 하면 하루가 지났음을 체크해 주어야 했습니다. 
그래서 함수를 만들어서 함수가 한번 실행 될 때마다 하루가 지나가는 방식으로 식을 만들었습니다. 
"""
n, m, h = map(int, input().split())
board2 = []
board = []
for __ in range(h):
    for _ in range(m):  # 창고 만들기
        data = list(map(int, input().split()))
        board2.append(data)
    else:
        A = copy(board2)
        board2.clear()
        board.append(A)


dx = [1, -1, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]  # 4방위 탐색
dh = [1, -1]
queue = deque()
queue2 = deque()  # 일수를 구해야 해서 둘로 나눔
cnt = 0
for k in range(h):
    for i in range(m):  # 처음 1의 위치 저장
        for j in range(n):
            if board[k][i][j] == 1:
                queue.append([k, i, j])


def one_day_after():
    global cnt  # 날짜 세 주기
    cnt += 1
    while queue:  # 어제 날짜 토마토 전부 탐색
        A = queue.popleft()
        for i in range(4):  # 4방위 델타 탐색
            nh = A[0]
            nx = A[1] + dx[i]
            ny = A[2] + dy[i]
            if 0 <= nx and nx < m and 0 <= ny and ny < n:  # 범위를 넘지 않고
                if board[nh][nx][ny] == 0:  # 0이면
                    board[nh][nx][ny] = 1  # 내일 익는 토마토로 체크
                    queue2.append([nh, nx, ny])  # 다음날을 위해 저장
        for i in range(2):  # 4방위 델타 탐색
            nh = A[0] + dh[i]
            nx = A[1]
            ny = A[2]
            if 0 <= nh and nh < h:
                if board[nh][nx][ny] == 0:  # 0이면
                    board[nh][nx][ny] = 1  # 내일 익는 토마토로 체크
                    queue2.append([nh, nx, ny])  # 다음날을 위해 저장


one_day_after()
while queue2:
    queue = copy(queue2)  # 큐 이동
    queue2.clear()  # 초기화
    one_day_after()  # 끝날때까지 반복
end = False
for k in range(h):
    if end == False:
        for i in range(m):
            if 0 in board[k][i]:
                print(-1)
                end = True
                break
else:
    if end == False:
        print(cnt-1)  # 하루가 더 세져서 -1
