import sys

sys.stdin = open("8979.txt", "r")

N, M = map(int, input().split())

contry = []

for _ in range(N):
    a, b, c, d = list(map(int, input().split()))
    score = b * (10**30) + c * (10**20) + d * (10**10)
    # print(score)
    contry.append([score, a])

contry.sort()
# print(contry)

for i in range(N):
    if M == contry[i][1]:
        while True:
            if (i + 1) < N and contry[i][0] == contry[i + 1][0]:
                i += 1

            else:
                break
        print(N - i)
