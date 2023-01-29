import sys

sys.stdin = open("11660.txt", "r")

N, M = map(int, input().split())
table = []
for i in range(N):
    data = list(map(int, input().split()))
    table.append(data)

# table을 누적합으로 바꾸어 주기
for y in range(1, N):
    table[y][0] = table[y - 1][0] + table[y][0]
for x in range(1, N):
    table[0][x] = table[0][x - 1] + table[0][x]
for y in range(1, N):
    for x in range(1, N):
        table[y][x] += table[y - 1][x] + table[y][x - 1] - table[y - 1][x - 1]
#

answer_list = []
for i in range(M):
    y1, x1, y2, x2 = map(int, input().split())
    answer = 0
    answer += table[y2 - 1][x2 - 1]
    if y1 - 2 != -1:
        answer -= table[y1 - 2][x2 - 1]
    if x1 - 2 != -1:
        answer -= table[y2 - 1][x1 - 2]
    if x1 - 2 != -1 and y1 - 2 != -1:
        answer += table[y1 - 2][x1 - 2]
    answer_list.append(answer)

for a in answer_list:
    print(a)
