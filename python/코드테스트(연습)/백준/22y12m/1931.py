import sys

sys.stdin = open("1931.txt", "r")

N = int(input())
time = []
for i in range(N):
    data = list(map(int, input().split()))
    time.append(data)
time.sort()

last_time = 2**32

# print(time)
cnt = 1
for t in time:
    # print(t, last_time)
    if last_time <= t[0]:
        last_time = t[1]
        cnt += 1
    if last_time > t[1]:
        last_time = t[1]
print(cnt)

# 이렇게 간단한 식으로 회의 순서가 정리 될 줄은 몰랐는데 신기하다.
