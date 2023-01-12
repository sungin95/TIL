import sys

sys.stdin = open("2156.txt", "r")

from collections import deque

N = int(input())
g_list = [0]
for i in range(N):
    data = int(input())
    g_list.append(data)

# print(g_list)
dp = [0] * (N + 1)


list_ = deque()
list_2 = deque()

for k in range(3):
    list_.append([0, k])

if N == 1:
    print(g_list[1])
elif N == 2:
    print(g_list[1] + g_list[2])
else:
    list_2.append([g_list[1] + g_list[2], 0])
    list_2.append([0, 0])
    for i in range(1, N + 1):
        for j in range(3):
            a = list_.pop()
            if a[1] == 0:
                a[0] = dp[i - 2] + g_list[i]
                a[1] += 1
                list_.appendleft(a)
            elif a[1] == 1:
                a[0] = dp[i - 3] + g_list[i - 1] + g_list[i]
                b = list_2.pop()
                if a[0] < b[0]:
                    a[0] = b[0]
                list_2.appendleft(a)
                a[1] += 1
                list_.appendleft(a)
            elif a[1] == 2:
                a[1] = 0
                list_.appendleft(a)
            if dp[i] < list_[0][0]:
                dp[i] = list_[0][0]

    print(max(dp))
