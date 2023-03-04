import sys

sys.stdin = open("1238.txt", "r")

from heapq import heappop, heappush

INF = sys.maxsize
N, M, X = map(int, input().split())
town_time = [[] for i in range(N)]
town_to_X_distince = [INF for i in range(N)]
town_to_X_distince[X - 1] = 0
for _ in range(M):
    v1, v2, t = map(int, input().split())
    town_time[v1 - 1].append((t, v2 - 1))
# print(town_to_X_distince)
# print(town_time)

for case in range(N):
    if town_to_X_distince[case] == 0:
        pass
    else:
        heapqueue = []
        heappush(heapqueue, (0, case))
        visited = [INF for i in range(N)]
        visited[case] = 0
        while heapqueue:
            time, town = heappop(heapqueue)
            for t, to in town_time[town]:
                if visited[to] > time + t:
                    visited[to] = time + t
                    heappush(heapqueue, (time + t, to))
        # go = visited[X - 1]
        town_to_X_distince[case] = visited[X - 1]

heapqueue = []
heappush(heapqueue, (0, X - 1))
visited = [INF for i in range(N)]
visited[X - 1] = 0
while heapqueue:
    time, town = heappop(heapqueue)
    for t, to in town_time[town]:
        if visited[to] > time + t:
            visited[to] = time + t
            heappush(heapqueue, (time + t, to))

for d in range(N):
    if town_to_X_distince[d] != 0:
        town_to_X_distince[d] += visited[d]
print(max(town_to_X_distince))
