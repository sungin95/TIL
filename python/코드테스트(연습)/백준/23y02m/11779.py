import sys

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

stack = [(0, start - 1, [start])]
cost_list[start - 1] = 0
while stack:
    c, s, str_v = heappop(stack)
    if s == (end - 1):
        print(c)
        print(len(str_v))
        print(*str_v)
        break
    for i in Map_[s]:
        if cost_list[i[0]] > c + i[1]:
            cost_list[i[0]] = c + i[1]
            # 문자열로 하면 안되고 리스트로 해 줘야 통과를 한다. 왜 그런지는 모르겠다.
            str_v2 = str_v + [i[0] + 1]
            heappush(stack, (cost_list[i[0]], i[0], str_v2))
