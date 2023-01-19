from collections import deque

N, K = map(int, input().split())

min_cnt = 1000000
cnt = 0


def move(N, K):
    dict_ = {}
    global min_cnt
    global cnt
    qeueu = deque()
    qeueu.append((N, 0))
    cnt = 0
    while qeueu:
        cur = qeueu.popleft()
        if dict_.get(cur[0]) == None:
            dict_[cur[0]] = cur[1]
        else:
            if dict_[cur[0]] >= cur[1]:
                dict_[cur[0]] = cur[1]
            else:
                continue
        if cur[0] > K * 2 or cur[0] < 0:
            continue

        if cur[0] == K:
            if min_cnt >= cur[1]:
                min_cnt = cur[1]
                cnt += 1
            else:
                break
        qeueu.append((cur[0] + 1, cur[1] + 1))
        qeueu.append((cur[0] - 1, cur[1] + 1))
        qeueu.append((cur[0] * 2, cur[1] + 1))


if N > K:
    print(N - K)
    print(1)
else:
    move(N, K)
    print(min_cnt)
    print(cnt)
