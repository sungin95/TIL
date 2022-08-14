N = int(input())
connection = int(input())
grape = [[] for _ in range(N+1)] # !
visited = [False]*(N+1)
print(grape)
for _ in range(connection):
    v1, v2 = map(int, input().split())
    grape[v1].append(v2)
    grape[v2].append(v1)
print(grape)
start = 1
visited[start] = True
stack = [start]
while stack:
    current = stack.pop()
    for cur in grape[current]:
        if visited[cur] == False:
        # if not visited[cur]:
            visited[cur] = True
            stack.append(cur)
print(visited)
