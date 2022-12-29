import sys

sys.stdin = open("6118.txt", "r")

from collections import deque

N, M = map(int, input().split())

graph = []
visited = []

for i in range(N + 1):
    graph.append([])
    visited.append([False])

for i in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

queue = deque()
queue.append([1, 0])
visited[1] = True

answer_list = []
while queue:
    cur = queue.popleft()
    for i in graph[cur[0]]:
        if visited[i] is not True:
            visited[i] = True
            queue.append([i, cur[1] + 1])
            answer_list.append([i, cur[1] + 1])

answer = []
for i in answer_list:
    if answer_list[-1][1] == i[1]:
        answer.append(i)
answer.sort()
print(answer[0][0], answer[0][1], len(answer))
