import sys

sys.stdin = open("1149.txt", "r")

N = int(input())
home = []
for i in range(N):
    data = list(map(int, input().split()))
    home.append(data)

for i in range(1, N):
    home[i][0] += min(home[i - 1][1], home[i - 1][2])
    home[i][1] += min(home[i - 1][0], home[i - 1][2])
    home[i][2] += min(home[i - 1][0], home[i - 1][1])
print(min(home[-1]))
