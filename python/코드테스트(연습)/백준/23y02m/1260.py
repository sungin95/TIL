import sys

sys.stdin = open("1260.txt", "r")

from collections import deque

N, M, V = map(int, input().split())
visited = [[False for i in range(N)] for i in range(2)]
graph = [[] for i in range(N)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1 - 1].append(v2 - 1)
    graph[v2 - 1].append(v1 - 1)

for i in range(N):
    graph[i].sort()

stack = [V - 1]
visited[0][V - 1] = True
answer_stack = []

# DFS는 재귀함수로 돌려야 구현이 제대로 된다.
def dfs(V):
    answer_stack.append(V + 1)
    for i in graph[V]:
        if visited[0][i] == False:
            visited[0][i] = True
            dfs(i)


dfs(V - 1)

answer_deque = []
queue = deque()
queue.append(V - 1)
visited[1][V - 1] = True
while queue:
    cur = queue.popleft()
    answer_deque.append(cur + 1)
    for i in graph[cur]:
        if visited[1][i] == False:
            visited[1][i] = True
            queue.append(i)
print(*answer_stack)
print(*answer_deque)
