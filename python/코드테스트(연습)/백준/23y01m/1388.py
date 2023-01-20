import sys

sys.stdin = open("1388.txt", "r")

N, M = map(int, input().split())
patten = []
for i in range(N):
    data = list(input())
    patten.append(data)

cnt = 0
for i in range(N):
    new = True
    for j in range(M):
        if new == True and patten[i][j] == "-":
            cnt += 1
            new = False
        elif patten[i][j] == "|":
            new = True

for j in range(M):
    new = True
    for i in range(N):
        if new == True and patten[i][j] == "|":
            cnt += 1
            new = False
        elif patten[i][j] == "-":
            new = True
print(cnt)
