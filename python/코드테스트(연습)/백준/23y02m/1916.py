import sys

sys.stdin = open("11779.txt", "r")
from heapq import heappop, heappush

INF = sys.maxsize
N = int(input())
M = int(input())
Map_ = [[] for i in range(N)]
for i in range(M):
    v1, v2, cost = map(int, input().split())
    Map_[v1 - 1].append((v2 - 1, cost))
start, end = map(int, input().split())

cost_list = [INF] * N

stack = [(0, start - 1)]
cost_list[start - 1] = 0
answer_list = []
while stack:
    c, s = heappop(stack)
    if s == (end - 1):
        answer_list.append(c)
        break
    for i in Map_[s]:
        if cost_list[i[0]] > c + i[1]:
            cost_list[i[0]] = c + i[1]
            heappush(stack, (cost_list[i[0]], i[0]))

answer_list.sort()
print(answer_list[0])
