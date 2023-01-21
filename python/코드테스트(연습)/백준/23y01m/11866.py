from collections import deque

N, K = map(int, input().split())
josephus = deque()
for i in range(1, N + 1):
    josephus.append(i)
cnt = 0
answer_list = []
while josephus:
    cnt += 1
    if cnt % K == 0:
        a = josephus.popleft()
        answer_list.append(a)
    else:
        a = josephus.popleft()
        josephus.append(a)
answer = "<"
for an in answer_list:
    answer += str(an)
    answer += ", "
else:
    answer = answer[:-2]
    answer += ">"
print(answer)
