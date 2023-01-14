import sys

sys.stdin = open("1.txt", "r")

N = int(input())
data = list(map(int, input().split()))
dp = [0 for i in range(5)]
# print(dp)
cnt = 0
max_ = 0
for i in data:
    if i == 1:
        cnt += 1
    else:
        cnt -= 1
    if cnt < 0:
        cnt = 0
    if max_ < cnt:
        max_ = cnt
cnt = 0
for i in data:
    if i == 2:
        cnt += 1
    else:
        cnt -= 1
    if cnt < 0:
        cnt = 0
    if max_ < cnt:
        max_ = cnt
print(max_)
