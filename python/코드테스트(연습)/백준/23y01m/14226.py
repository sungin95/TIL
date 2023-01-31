from collections import deque

S = int(input())

visited = [[0 for i in range(S + 1)] for i in range(S * 2)]
queue = deque()
# 화면 값, 클립보드, cnt
imo = 1
clip = 0
cnt = 1
queue.append((imo, clip, cnt))

visited[imo][clip] = cnt
while queue:
    if clip < S != 0 and visited[S][clip]:
        print(visited[S][clip] - 1)
        break
    imo, clip, cnt = queue.popleft()
    if 0 <= imo - 1 and (imo + clip) < 2 * S and clip < S:
        queue.append((imo, imo, cnt + 1))
        if visited[imo + clip][clip] == 0:
            queue.append((imo + clip, clip, cnt + 1))
            visited[imo + clip][clip] = cnt + 1
        if visited[imo - 1][clip] == 0:
            queue.append((imo - 1, clip, cnt + 1))
            visited[imo - 1][clip] = cnt + 1
