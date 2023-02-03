import sys

sys.stdin = open("1039.txt", "r")

from collections import deque

N, K = input().split()

K = int(K)

queue = deque()
queue.append((N, 0))
s_check = -1
try:
    while True:
        cur, cnt = queue.popleft()
        cur = list(cur)
        if cnt == K:
            break
        if s_check != cnt:
            max_set = set()
            s_check = cnt
        for i in range(len(N)):
            for j in range(i + 1, len(N)):
                if N[j] != "0":
                    new = cur.copy()
                    new[i] = cur[j]
                    new[j] = cur[i]
                    new2 = "".join(new)

                    a = len(max_set)
                    max_set.add((new2, cnt + 1))
                    if a != len(max_set):
                        queue.append((new2, cnt + 1))
    answer = max(max_set)
    print(int(answer[0]))
except:
    print(-1)
