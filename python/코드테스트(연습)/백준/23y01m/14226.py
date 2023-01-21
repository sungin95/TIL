from collections import deque

S = int(input())

visited = [0 for i in range(S * 2)]
queue = deque()
queue.append((1, 0, 1))

while queue:
    if visited[S] != 0:
        print(visited[S] - 1)
        break
    cur = queue.popleft()
    visited[1] = 1
    if 0 <= cur[0] - 1 and (cur[0] + cur[1]) < 2 * S:
        queue.append((cur[0], cur[0], cur[2] + 1))
        if visited[cur[0] + cur[1]] == 0 or visited[cur[0] + cur[1]] == cur[2] + 1:
            queue.append((cur[0] + cur[1], cur[1], cur[2] + 1))
            visited[cur[0] + cur[1]] = cur[2] + 1
        if visited[cur[0] - 1] == 0 or visited[cur[0] - 1] == cur[2] + 1:
            queue.append((cur[0] - 1, cur[1], cur[2] + 1))
            visited[cur[0] - 1] = cur[2] + 1
