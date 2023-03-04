import sys

sys.stdin = open("1717.txt", "r")
N, M = map(int, input().split())
calc = [{i} for i in range(N + 1)]
answer_list = []

for _ in range(M):
    ty, v1, v2 = map(int, input().split())
    if ty == 0:
        for i in calc[v2]:
            calc[v1].add(i)

        for i in calc[v2]:
            calc[i] = calc[v1]
    if ty == 1:
        if v2 in calc[v1]:
            answer_list.append("YES")
        else:
            answer_list.append("NO")
for answer in answer_list:
    print(answer)


# N, M = map(int, input().split())
# calc = [[] for i in range(N + 1)]
# answer_list = []
# for _ in range(M):
#     ty, v1, v2 = map(int, input().split())
#     if ty == 0:
#         calc[v1].append(v2)
#         calc[v2].append(v1)
#     elif ty == 1:
#         stack = []
#         stack.append(v1)
#         visited = [[False] for i in range(N + 1)]
#         visited[v1] = True
#         while stack:
#             cur = stack.pop()
#             if cur == v2:
#                 answer_list.append("YES")
#                 break
#             for cal in calc[cur]:
#                 if visited[cal] == False:
#                     stack.append(cal)
#                     visited[cal] = True

#         else:
#             answer_list.append("NO")
# for answer in answer_list:
#     print(answer)
