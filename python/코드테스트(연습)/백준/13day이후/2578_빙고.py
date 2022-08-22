import sys
sys.stdin = open("2578.txt","r")

board = []
for _ in range(5):
    bingo = input().split()
    board = board + bingo
answer = 0
cnt = 0
call_bingo = 0
END = False
y_list = [[],[],[],[],[]] # 답을 하나하나 세 주는게 오히려 편할거 같아서 
x_list = [[],[],[],[],[]] # X축 5개 Y축 5개 대각선 2개 체크시트를 만들었습니다. 
diagonal_list = [[],[]]
for _ in range(5):
    count = input().split()
    for c in count:
        cnt += 1
        a = board.index(c)
        y = a//5
        x = a%5 # 이 작업을 통해 좌표를 알 수 있습니다. 

        y_list[y].append("o") # y축 카운트 
        if len(y_list[y]) == 5:
            call_bingo += 1

        x_list[x].append("o") # x축 카운트 
        if len(x_list[x]) == 5:
            call_bingo += 1

        if x == y:
            diagonal_list[0].append("o")
            if len(diagonal_list[0]) == 5:
                call_bingo += 1
        if x + y == 4:
            diagonal_list[1].append("o")
            if len(diagonal_list[1]) == 5:
                call_bingo += 1

        if END == False: # 최초 3빙고 정보를 얻기 위해
            if call_bingo >= 3: # 빙고는 3 이상
                END = True
                answer = cnt
print(answer)
