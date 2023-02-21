import sys

sys.stdin = open("10282.txt", "r")

from heapq import heappop, heappush

answer_list = []
INF = sys.maxsize
T = int(input())
for t in range(T):
    # 갯수, 관계수, 최초 감염 컴퓨터
    N, D, C = map(int, input().split())

    computer = [[] for i in range(N)]
    for _ in range(D):
        # v1,v2,감염에 걸리는 시간
        a, b, s = map(int, input().split())
        computer[b - 1].append((a - 1, s))

    visited = [INF for i in range(N)]
    visited[C - 1] = 0

    heapqueue = [(0, C - 1)]
    last_time = 0
    while heapqueue:
        time, cur = heappop(heapqueue)
        for c, t in computer[cur]:
            if visited[c] > time + t:
                heappush(heapqueue, (time + t, c))
                visited[c] = time + t
    answer = []
    for v in visited:
        if v < 1000000000000:
            answer.append(v)
    print(answer)
    answer_list.append([len(answer), max(answer)])

for a in answer_list:
    print(*a)
