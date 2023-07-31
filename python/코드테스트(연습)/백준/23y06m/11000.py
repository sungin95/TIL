import sys

sys.stdin = open("11000.txt", "r")

import heapq

N = int(input())
class_schedule = []
for i in range(N):
    start_time, end_time = map(int, input().split())
    class_schedule.append((start_time, end_time))

class_schedule.sort()


heap = []
max_len_heap = 0

for start, end in class_schedule:
    while heap:
        if heap[0] <= start:
            heapq.heappop(heap)
        else:
            break
    heapq.heappush(heap, end)
    if max_len_heap < len(heap):
        max_len_heap = len(heap)

print(max_len_heap)
