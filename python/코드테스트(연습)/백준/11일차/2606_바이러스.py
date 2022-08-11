N = int(input())
T = int(input())
graph = []
for _ in range(N+1):
    graph.append([])

visited = [False] * (N+1)
for t in range(T):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
    
start = 1
stack = [start]
visited[start] = True
cnt = 0
while stack:
    cur = stack.pop()
    for adj in graph[cur]:
        if not visited[adj]:
            visited[adj] = True
            cnt += 1
            stack.append(adj)
print(cnt)