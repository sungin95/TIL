import sys

sys.stdin = open("1202.txt", "r")

import heapq

N, K = map(int, input().split())
jewelry = [[*map(int, input().split())] for _ in range(N)]
bag = [min(int(input()), 1000000) for _ in range(K)]

jewelry.sort(reverse=True)
bag.sort()

jewelry_bag = []
answer = 0
# 작은보석을 담을 수 있는 가방에서 부터 담아준다.
for b in bag:
    # b 무게 이하 모두 넣기(value만 저장)
    while jewelry and b >= jewelry[-1][0]:
        heapq.heappush(jewelry_bag, -jewelry[-1][1])
        jewelry.pop()

    # b무게 이하중 최고 밸류(선택하면 빼주고)
    if jewelry_bag:
        answer += heapq.heappop(jewelry_bag)


print(-answer)
