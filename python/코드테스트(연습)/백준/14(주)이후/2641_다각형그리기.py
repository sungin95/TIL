from collections import deque

N = int(input())
sample = deque(map(int, input().split()))
M = int(input())
answer_list = []
for i in range(M):
    data_reverse = []
    data = deque(map(int, input().split()))
    answer_list.append(list(data))
    for d in list(data)[::-1]:
        if d == 2:
            data_reverse.append(4)
        else:
            data_reverse.append(abs((d+2)%4))
    data_reverse = deque(data_reverse)
    for j in range(N):
        if sample == data or sample == data_reverse:
            break
        else:
            a = data.popleft()
            data.append(a)
            b = data_reverse.popleft()
            data_reverse.append(b)
    else:
        answer_list.pop()

print(len(answer_list))
for ans in answer_list:
    print(*ans)