import sys
sys.stdin = open("1987.txt","r")
input = sys.stdin.readline

Y,X = map(int, input().split())
board = []
alphabet = set()
for y in range(Y):
    data = input()
    for i in data:
        alphabet.add(i)
    board.append([])
    for chr in data:
        board[y].append(chr)
dy = [1,-1,0,0]
dx = [0,0,1,-1]
current = [0,0]
def bfs():
    for i in range(4):
        ny = current[0] + dy[i]
        nx = current[1] + dx[i]
        if 0 > ny or ny >= Y or 0 > nx or nx >= X:
            pass                                   
        else:
            if board[ny][nx] not in visited:
                stack.append([board[ny][nx],[ny,nx],cnt])