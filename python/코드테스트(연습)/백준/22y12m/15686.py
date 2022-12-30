import sys

sys.stdin = open("15686.txt", "r")

from itertools import combinations

N, M = map(int, input().split())
# 지도 만들기
map_ = []
for i in range(N):
    data = input().split()
    map_.append(data)

# 치킨집과 집 위치 알아내기
chickin_list = []
home_list = []
for i in range(N):
    for j in range(N):
        # i,j는 좌표
        if map_[i][j] == "1":
            # 0은
            home_list.append([0, i, j])
        elif map_[i][j] == "2":
            chickin_list.append([0, i, j])

# 치킨 폐업
for c in chickin_list:
    for h in home_list:
        # 각 치킨집과 집 거리 측정후 모두 합쳐주기
        x = abs(c[1] - h[1])
        y = abs(c[2] - h[2])
        c[0] += x + y

chickin_list_conbi = []
chickin_list.sort()
chickin_list.reverse()

# M개
# for m in range(M):
#     a = chickin_list.pop()
#     chickin_list_conbi.append(a)

# # 거리가 같은 값이 있으면 조합 만들기
# while chickin_list:
#     a = chickin_list.pop()
#     if a[0] == chickin_list_conbi[-1][0]:
#         chickin_list_conbi.append(a)
#     else:
#         break

conbi = list(combinations(chickin_list, M))
# print(conbi)
# 집에서 치킨 거리 최소값
answer_list = []
for conbi__ in conbi:
    answer = 0
    for h in home_list:
        min_di = []
        for c in conbi__:
            x = abs(c[1] - h[1])
            y = abs(c[2] - h[2])
            min_di.append(x + y)
        h[0] = min(min_di)
        answer += min(min_di)
    answer_list.append(answer)
# print(answer_list)
print(min(answer_list))

# 결국 문제는 내가 문제를 읽고 생각을 잘못하고 조건을 하나 더 넣었다. 그게 문제라고 생각을 못해서 많이 헤맸다.
# (오히려 여기를 고려하지 않은 친구들을 속으로 나무랐던거 같다. 반성해야 겠다. )
