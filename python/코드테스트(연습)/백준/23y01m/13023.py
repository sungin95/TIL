import sys
from pprint import pprint

# https://emhaki.tistory.com/33
sys.stdin = open("13023.txt", "r")
# from collections import deque

# N, M = map(int, input().split())
# graf_ = []
# for i in range(N):
#     # 왼쪽은 경로, 오른쪽은 visited
#     graf_.append([[], []])
# for i in range(M):
#     v1, v2 = map(int, input().split())
#     graf_[v1][0].append(v2)
#     graf_[v2][0].append(v1)


# def connected_friend(start, graf):
#     stack = deque()
#     stack.append(start)
#     if start not in graf[start][1]:
#         graf[start][1].append(start)
#     while stack:
#         cur = stack.popleft()
#         for i in graf[cur][0]:
#             if i not in graf[cur][1]:
#                 if len(graf[i][1]) != 0:
#                     graf[i][1] = []
#                 for j in graf[cur][1]:
#                     graf[i][1].append(j)
#                 graf[i][1].append(i)
#                 stack.append(i)
#                 if len(graf[i][1]) == 5:
#                     print(start, i)
#                     return 1
#     return 0


# answer = 0
# for i in range(N):
#     answer = connected_friend(i, graf_)
#     # 그래프를 초기화
#     pprint(graf_)
#     for j in graf_:
#         j[1] = []
#     if answer == 1:
#         break
# print(answer)


N, M = map(int, input().split())
graf_ = []
visited = [False]
for i in range(N):
    graf_.append([])
    visited.append(False)
for i in range(M):
    v1, v2 = map(int, input().split())
    graf_[v1].append(v2)
    graf_[v2].append(v1)


check = [False]


def all_case(i, cnt):
    if cnt == 4:
        check[0] = True
        return
    for j in graf_[i]:
        if visited[j] == False:
            visited[j] = True
            # print(cnt, visited)
            all_case(j, cnt + 1)
            # print(cnt, visited)
            visited[j] = False


for i in range(N):
    visited[i] = True
    # print(visited)
    all_case(i, 0)
    visited[i] = False
    if check[0] == True:
        print(1)
        break
else:
    print(0)
