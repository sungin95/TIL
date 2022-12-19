import sys

sys.stdin = open("12847.txt", "r")
from collections import deque


N, M = map(int, input().split())
work_queue = deque(map(int, input().split()))
sum_ = 0
work = deque()
answer_list = []
# 처음
for i in range(M):
    work_i = work_queue.popleft()
    work.append(work_i)
else:
    answer_list.append(sum(work))
# work를 맨 왼쪽과 맨 오른쪽을 더한다.
for j in range(N - M):
    work_j = work_queue.popleft()  # 더하는 값
    a = work.popleft()  # 빼는값
    work.append(work_j)  # work 다시 완성

    answer_list.append(answer_list[-1] + work_j - a)

print(max(answer_list))
