n = int(input())

stair = [[0] * 10 for i in range(n + 1)]

for i in range(1, 10):
    stair[1][i] = 1

if n == 1:
    print(9)
else:
    for i in range(2, n + 1):
        stair[i][0] = stair[i - 1][1] % 1000000000
        for j in range(1, 9):
            stair[i][j] = (stair[i - 1][j + 1] + stair[i - 1][j - 1]) % 1000000000
        stair[i][9] = stair[i - 1][8] % 1000000000
    print(sum(stair[-1]) % 1000000000)
