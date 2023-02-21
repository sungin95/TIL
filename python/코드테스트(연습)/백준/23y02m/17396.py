import sys
from heapq import heappop, heappush

INF = sys.maxsize
sys.stdin = open("17396.txt", "r")

N, M = map(int, input().split())
danger = list(map(int, input().split()))
danger.pop()
danger.append(0)
visited = [INF for i in range(N)]
graph = [[] for i in range(N)]
for i in range(M):
    v1, v2, c = map(int, input().split())
    graph[v1].append((c, v2))
    graph[v2].append((c, v1))

heapqueue = [(0, 0)]
visited[0] = 0


check = False
for v, i in graph[N - 1]:
    if danger[i] == 0:
        check = True
if check == True:
    answer = -1
    while heapqueue:
        t, v = heappop(heapqueue)
        if v == (N - 1):
            answer = t
            break
        # 여기가 중요!!! 시간을 줄여야 한다.
        elif visited[v] < (t):
            continue
        for ti, vi in graph[v]:
            if danger[vi] != 1 and visited[vi] > (t + ti):
                heappush(heapqueue, (t + ti, vi))
                visited[vi] = t + ti

    print(answer)
else:
    print(-1)
