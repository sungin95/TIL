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
# 기본적으로 바이러스와 델타탐색을 섞어서 문제를 풀었습니다. 
cnt = 1 # 칸수
stack = [[board[0][0],[0,0],cnt]] # 시작은 0,0부터
# stack[0]는 알파벳(visited 에 사용할 예정 + 순서가 있습니다.)
# stack[1] 델타탐색 ny, nx를 만들기 위해 만들었습니다. 
# stack[2] 은 길을 가다가 백을 하면 칸수를 그 길을 기준으로 다시 세야 했습니다. 
# 그래서 따로 넣어주어 관리를 했습니다. 
visited = []
max_ = 0 # 최대 칸수
while stack:
    stack_a = stack.pop()
    cnt = stack_a[2]
    while len(visited) >= cnt: # 탐색하다 길 못찾아 백하면 그에 맞게 visited 리셋
        visited.pop()
    visited.append(stack_a[0]) # 내가 간 길에 순서에 맞게 기록이 되어 있습니다. 
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    # print(cnt)
    # print(visited)
    # print(stack)
    if max_ < cnt:
        max_ = cnt # 맥스 최신화 
        if max_ == (len(alphabet)-1): # 이때 max값이 속에 포함되어 있는 알파벳 갯수보다 크지 않습니다. -1은 /n가 생겨서 빼주었습니다. 
            break      # 시간을 줄이기 위해 만들었습니다. 
    cnt += 1
    for i in range(4):
        ny = stack_a[1][0] + dy[i]
        nx = stack_a[1][1] + dx[i]
        if 0 > ny or ny >= Y or 0 > nx or nx >= X: # 탐색 시간을 조금이라도 줄이기 위해 
            pass                                   # 하나의 조건만 만족해도 넘어가게 했습니다. 
        else:
            if board[ny][nx] not in visited:
                stack.append([board[ny][nx],[ny,nx],cnt])
print(max_)

