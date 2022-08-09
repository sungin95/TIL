from pprint import pprint


N = int(input())
M = int(input())
arr = [[0]*N for _ in range(N)]
for m in range(M):
    a,b = map(int, input().split())
    arr[a-1][b-1] = 1
    arr[b-1][a-1] = 1

connection = [0]

while True:
    cn = len(connection)
    for j in connection:
        for i in range(N):
            if arr[j][i] == 1:
                connection.append(i)
                connection=list(set(connection))
    else:
        cn2 = len(set(connection))
        if cn == cn2:
            break
print(len(connection)-1)