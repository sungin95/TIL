import sys

sys.stdin = open("1753.txt", "r")
INF = sys.maxsize
from heapq import heappop, heappush

N, M = map(int, input().split())
start = int(input())
v = [[] for i in range(N)]
for _ in range(M):
    v1, v2, cost = map(int, input().split())
    v[v1 - 1].append((v2 - 1, cost))

cost_list = [INF for i in range(N)]
stack = [(0, start - 1)]
cost_list[start - 1] = 0
while stack:
    cur_cost, cur = heappop(stack)
    for n, c in v[cur]:
        if cost_list[n] > cur_cost + c:
            cost_list[n] = cur_cost + c
            heappush(stack, (cur_cost + c, n))

for a in cost_list:
    if a > 30000000:
        print("INF")
    else:
        print(a)
