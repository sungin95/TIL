t = int(input())
answer_list = []
color_paper = []
board = []
for i in range(1001):
    board.append([])
    for j in range(1001):
        board[i].append(1)

for i in range(t):
    paper = list(map(int,input().split()))
    color_paper.append(paper)

for i in range(t):
    width = 0
    a = color_paper.pop()
    for i in range(a[0], a[0] + a[2]):
        for j in range(a[1], a[1] + a[3]):
            if board[i][j] == 1:
                width += 1
                board[i][j] = 0
    answer_list.append(width)
for ans in answer_list[::-1]:
    print(ans)


