import sys
sys.stdin = open("1987.txt","r")
input = sys.stdin.readline

Y,X = map(int, input().split())
board = []
for y in range(Y):
    data = input()
    board.append([])
    for chr in data:
        board[y].append(chr)
cnt = 1
stack = [[board[0][0],[0,0],cnt]]
visited = []
max_ = 0
while stack:
    stack_a = stack.pop()
    cnt = stack_a[2]
    while len(visited) >= cnt:
        visited.pop()
    visited.append(stack_a[0])
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    print(cnt)
    print(visited)
    print(stack)
    if max_ < cnt:
        max_ = cnt
        if max_ == 26:
            break
    cnt += 1
    for i in range(4):
        ny = stack_a[1][0] + dy[i]
        nx = stack_a[1][1] + dx[i]
        if 0 > ny or ny >= Y or 0 > nx or nx >= X:
            pass
        else:
            if board[ny][nx] not in visited:
                stack.append([board[ny][nx],[ny,nx],cnt])
print(max_)

