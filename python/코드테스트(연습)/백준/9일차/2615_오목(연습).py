from pprint import pprint

dy = [0, 1, -1, 1]
dx = [1, 0, 1, 1]
BLACK = 1
WHITE = 2
N = 19

board = []
for _ in range(N):
    temp_list = list(map(int, input().split()))
    board.append()

pprint(board)
for y in range(N):
    for x in range(N):

        for d in range(4):
            stone_count = 0

            ny = y + dy[d]
            nx = x + dx[d]

            while True:

                if not(-1 < ny < N and -1 < nx < N):
                    break
                
                if not(board[y][x] == board[ny][ny]):
                    break

                stone_count += 1

                ny = ny + dy[d]
                nx = nx + dx[d]

