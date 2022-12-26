import sys

sys.stdin = open("11047.txt", "r")


N, K = map(int, input().split())
coin = []
for _ in range(N):
    data = int(input())
    coin.append(data)

cnt = 0
while K != 0:
    cnt += 1
    for i in range(N):
        if K >= coin[i]:
            pass
        else:
            K -= coin[i - 1]
            break
    else:
        K -= coin[-1]
print(cnt)
