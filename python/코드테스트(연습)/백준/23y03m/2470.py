import sys

sys.stdin = open("2470.txt", "r")
INF = sys.maxsize
from bisect import bisect_left

N = int(input())
N_list = sorted(list(map(int, input().split())))

to_zero = INF
# to_zero_list = []

for z in range((len(N_list))):
    try:
        for i in [-1, 0, 1]:
            if N_list[z] != N_list[bisect_left(N_list, -N_list[z]) + i]:
                # print(
                #     abs(N_list[z] + N_list[bisect_left(N_list, -N_list[z]) + i]),
                #     N_list[z],
                #     N_list[bisect_left(N_list, -N_list[z]) + i],
                # )
                if to_zero > abs(
                    N_list[z] + N_list[bisect_left(N_list, -N_list[z]) + i]
                ):
                    to_zero = abs(
                        N_list[z] + N_list[bisect_left(N_list, -N_list[z]) + i]
                    )
                    to_zero_list = []
                    to_zero_list.append(N_list[z])
                    to_zero_list.append(N_list[bisect_left(N_list, -N_list[z]) + i])
    except:
        pass
        # print("error")
to_zero_list.sort()
# print(to_zero)
print(*to_zero_list)
