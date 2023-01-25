from collections import deque

N, K = map(int, input().split())
visited = [False for i in range(100001)]


def move(N, K):
    qeueu = deque()
    qeueu.append((N, 0, [N]))
    visited[N] = True
    while qeueu:
        cur, cnt, passed = qeueu.popleft()
        if cur == K:
            print(cnt)
            print(*passed)
            break
        for c in [cur + 1, cur - 1, cur * 2]:
            if 0 < c < 100001 and visited[c] == False:
                visited[c] = True
                qeueu.append((c, cnt + 1, passed + [c]))


if N > K:
    print(N - K)
    for i in range(N, K - 1, -1):
        print(i, end=" ")
else:
    move(N, K)
