from collections import deque
from copy import copy

N, K = map(int, input().split())
check = {
    N: 0,
}
queue = deque()
queue.append([0+N, 0])
if N >= K:
    print(abs(N-K))

else:
    if N == 0:
        queue.popleft()
        queue.append([1, 1])
        check[1] = 1
    while True:
        A = queue.popleft()
        # print(A)
        if A[0] == K:
            print(A[1])
            break
        A[1] += 1  # cnt
        if A[0] >= K+2:
            continue
        if A[0] == 0:
            continue
        B = copy(A[0]-1)
        if check.get(B) == None:
            check[B] = A[1]
            queue.append([B, A[1]])
        C = copy(A[0] + 1)
        if check.get(C) == None:
            check[C] = A[1]
            queue.append([C, A[1]])
        D = copy(2*A[0])
        if check.get(D) == None:
            check[D] = A[1]
            queue.append([D, A[1]])
# print(check)
